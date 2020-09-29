import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from firebase import firebase
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import time
import os
import cv2
import numpy as np


idSelected = ""
name = ""
mobileNo = ""
logInWindow = Tk()
font = cv2.FONT_HERSHEY_PLAIN
firebase = firebase.FirebaseApplication('https://m-card-2ac54.firebaseio.com/', None)

localtime=time.asctime(time.localtime(time.time()))




# load2 = Image.open("login.png")
# render2 = ImageTk.PhotoImage(load2)
# img2 = Label(logInWindow, image=render2)
# img2.image = render
# img2.place(x=260, y=50, width = 460, height=800)


def loginMethodone():
    print("Hello")


def scanQrMethod():
    print("Scan Comp")





canvas = Canvas(logInWindow,width = 1284,height = 724)
canvas.configure(bg = '#2E2F30' )
load = Image.open("background.jpg")
ph = ImageTk.PhotoImage(load)
canvas.create_image(0,0, image=ph, anchor=NW)
canvas.pack(expand = YES,fill = BOTH)

canvas.create_rectangle(210, 150,510, 500, fill="#008AAF",width = 3,outline = "#FFFFFF")



t1 = Entry(font=('ariel',15))
t2 = Entry(font=('ariel',15),show="*")

t1.insert(0,"ID")
t2.insert(0,"Password")
t1.place(x = 260,y = 200)
t2.place(x=260, y = 250)
timeView = Label(logInWindow, font=( 'aria' ,20, ),text= " " + localtime,fg="steel blue",anchor=W)
MainLabel = Label(logInWindow,text = "WELCOME TO MEDICARD",bg = "#FFFFFF")
MainLabel.config(font = ("Courier",38))
orLabel = Label(logInWindow,text = "OR",bg = '#008AAF',font = ('aria',20),fg = "white")



def loginMethodone():
    os.system("python3 progressBar.py")
    patientId = t1.get()
    patientPass = t2.get()
    if patientId != "ID" or patientPass  != "Password" or patientPass != "" or patientId != "":
        result = firebase.get('/Auth/' + patientId, None)
        print(result)
        if result != None:
            password  = result["password"]
            print(password)
            if password == "":
                t1.delete(0,"end")
                t1.insert(0,"Wrong ID")
                t2.delete(0,'end')
            elif password == patientPass:
                print("Go next")
                idSelected = patientId
                name = result["name"]
                mobileNo = result["mobil"]
                
                profileInfoList = [name,mobileNo,idSelected]
                nextPage(profileInfoList)
                print("Enter")
            else:
                t2.delete(0,"end")
                t2.insert(0,"Wrong Password")
        else:
            t1.delete(0,"end")
            t1.insert(0,"Wrong ID")

    else:
        
        t1.insert(0,"Enter ID")
        t2.insert(0,"Enter Password")








def scanQrMethod():
    cap = cv2.VideoCapture(0)
    get = 0
    while True:
            _, frame = cap.read()
            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                # print("Data",obj.data)
                result1 = obj.data.decode("utf-8")
                # print(result)
                if(result1 != ""):
                    result = firebase.get('/Auth/' + result1, None)
                    idSelected = result1
                    name = result["name"]
                    mobileNo = result["mobil"]
                   
                    # self.name.insert(END,result["name"])
                    # self.Mobile.insert(END,result["mobil"])

                    print(result)
                    get = 1
                    cv2.destroyAllWindows()
                    break
                
                cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                   (255, 0, 0), 3)
         
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27 or get == 1:
                cv2.destroyAllWindows() 
                break



loginButton = Button(logInWindow, bd=10 ,fg="black",pady = 10,font=('ariel' ,16),width=13, text="LOGIN", bg="powder blue",command=loginMethodone)
scanButon = Button(logInWindow, bd=10 ,fg="black",font=('ariel' ,16),width=13, text="SCAN QR", bg="powder blue",command=scanQrMethod)
MainLabel.place(y = 35,x = 680,anchor = "center")
timeView.place(y = 12,x = 1160,anchor = "center")
loginButton.place(x = 260,y = 300,width = 212,height = 30)
orLabel.place(x = 260,y = 340,width = 212,height = 30)
scanButon.place(x = 260,y = 380,width = 212,height = 30)
# img = ImageTk.PhotoImage(Image.open("block.png"))
panel = Label(logInWindow,bg = "#2E2F30")
panel.place(x = 210,y = 150,width = 300,height = 350)

def ulock():
    password = unlockPassword.get()
    filee = open("doctorinfo.txt","r")
    stri = filee.read().split("_")
    print(stri[3])
    if password == stri[3]:
         panel.destroy()
         ulockButton.destroy()
         unlockPassword.destroy()
    else:
        unlockPassword.delete(0,"end")
        unlockPassword.insert(0,"Wrong Password")
        



filee2 = open("doctorinfo.txt","r")
stri2 = filee2.read().split("_")




ulockButton = Button(logInWindow,text = "UNLOCK",command = ulock)
ulockButton.pack()
unlockPassword = Entry(font=('ariel',15),show = "*")
unlockPassword.insert(0,"Enter password")
unlockPassword.pack()
unlockPassword.place(x = 260,y = 280,width = 212,height = 30)
ulockButton.place(x = 260,y = 340,width = 212,height = 30)
doctorLabel = Label(logInWindow,text = stri2[0],bg = '#008AAF',font = ('aria',20),fg = "white")
doctorLabel.place(x = 260,y = 200,width = 212,height = 30)
doctorID = Label(logInWindow,text = stri2[2],bg = '#008AAF',font = ('aria',20),fg = "white")
doctorID.place(x = 260,y = 240,width = 212,height = 30)






def nextPage(profileInfoList):
    os.system("python3 mainActivity.py " + str(profileInfoList))

    # newWindow = Tk()
    # mycolor2 = '#2E2F30'
    # newWindow.configure(bg=mycolor2)
    # newWindow.title('MED-CARD')
    # newWindow.geometry("1284x724+10+10")
    # nameViewOfUser = Label(newWindow, font=( 'aria' ,20, ),text= nameTwo,fg="steel blue",anchor=W)
    # nameViewOfUser.place(y = 12,x = 1200,anchor = "center")
    # newTimeView = Label(newWindow, font=( 'aria' ,20, ),text= " "+ localtime,fg="steel blue",anchor=W)
    # newTimeView.place(y = 20,x = 1050)
    # MainLabel2 = Label(newWindow,text = "WELCOME TO MEDICARD",bg = "#FFFFFF")
    # MainLabel2.config(font = ("Courier",38))
    # MainLabel2.place(y = 35,x = 680,anchor = "center")

    # nameOfPrescription = Entry(newWindow)
    # nameOfPrescription.insert(0,"Enter name")
    # nameOfPrescription.place(x = 260,y = 150)
    # p1 = Entry(newWindow)
    # p2 = Entry(newWindow)
    # p3 = Entry(newWindow)
    # p4 = Entry(newWindow)
    # p1.place(x =260,y = 200 )
    # p2.place(x = 260,y = 250)
    # p3.place(x = 260,y = 300)
    # p4.place(x = 260,y = 350)
    # def getData():
    #     nameOfPres = nameOfPrescription.get()
    #     pe1 = p1.get()
    #     pe2 = p2.get()
    #     pe3 = p3.get()
    #     pe4 = p4.get()
    #     dictionary = {}
    #     dictionary["1"]  = nameOfPres
    #     dictionary["2"]  = pe1
    #     dictionary["3"]  = pe2
    #     dictionary["4"]  = pe3
    #     dictionary["5"]  = pe4
    #     timelocal = localtime.split(" ")
    #     man = timelocal[2] + "_" +  timelocal[1] + "_" + timelocal[4]
    #     sendData = firebase.put("Users/" + idSelectedFor + "/",man,dictionary)
    #     result = firebase.post('Users/' + idSelectedFor + "/Dates", data=man, params={'demo': 'demo'})


    
    # sendButton = Button(newWindow,text = "Send Data",command = getData)
    # sendButton.place(x = 260,y = 400)


mycolor2 = '#2E2F30'
logInWindow.configure(bg=mycolor2)
logInWindow.title('MED-CARD')
logInWindow.geometry("1284x724+10+10")

logInWindow.mainloop()