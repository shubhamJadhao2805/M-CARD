# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import os
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 807)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 50, 1441, 851))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("backgroundimage.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.portalbackground = QtWidgets.QLabel(Dialog)
        self.portalbackground.setGeometry(QtCore.QRect(-20, 0, 1471, 61))
        self.portalbackground.setText("")
        self.portalbackground.setPixmap(QtGui.QPixmap("upperbanner.png"))
        self.portalbackground.setScaledContents(True)
        self.portalbackground.setObjectName("portalbackground")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(65, 89, 221)")
        self.label_2.setObjectName("label_2")
        self.backimage = QtWidgets.QLabel(Dialog)
        self.backimage.setGeometry(QtCore.QRect(530, 190, 421, 581))
        self.backimage.setText("")
        self.backimage.setPixmap(QtGui.QPixmap("loginpageback.png"))
        self.backimage.setScaledContents(True)
        self.backimage.setObjectName("backimage")
        self.icon = QtWidgets.QLabel(Dialog)
        self.icon.setGeometry(QtCore.QRect(690, 210, 111, 111))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("usericon.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.welcometomcard = QtWidgets.QLabel(Dialog)
        self.welcometomcard.setGeometry(QtCore.QRect(640, 340, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.welcometomcard.setFont(font)
        self.welcometomcard.setStyleSheet("color:rgb(255, 255, 255)")
        self.welcometomcard.setObjectName("welcometomcard")
        self.nameField = QtWidgets.QTextEdit(Dialog)
        self.nameField.setGeometry(QtCore.QRect(580, 400, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nameField.setFont(font)
        self.nameField.setObjectName("nameField")
        self.mobileNoField = QtWidgets.QTextEdit(Dialog)
        self.mobileNoField.setGeometry(QtCore.QRect(580, 460, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mobileNoField.setFont(font)
        self.mobileNoField.setObjectName("mobileNoField")
        self.doctorId = QtWidgets.QTextEdit(Dialog)
        self.doctorId.setGeometry(QtCore.QRect(580, 520, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.doctorId.setFont(font)
        self.doctorId.setObjectName("doctorId")
        self.password = QtWidgets.QTextEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(580, 580, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.createaccount = QtWidgets.QPushButton(Dialog)
        self.createaccount.setGeometry(QtCore.QRect(581, 640, 320, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.createaccount.setFont(font)
        self.createaccount.setStyleSheet("background-color:rgb(146, 35, 145);\n"
"color:rgb(255,255,255);\n"
"")
        self.createaccount.setObjectName("createaccount")
        self.medicard2020 = QtWidgets.QLabel(Dialog)
        self.medicard2020.setGeometry(QtCore.QRect(700, 720, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.medicard2020.setFont(font)
        self.medicard2020.setStyleSheet("color:rgb(255, 255, 255)")
        self.medicard2020.setObjectName("medicard2020")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.createaccount.clicked.connect(self.signMethod)

        #method for login
    def signMethod(self):
        name = self.nameField.toPlainText()
        mobileNo = self.mobileNoField.toPlainText()
        doctorId = self.doctorId.toPlainText()
        passw = self.password.toPlainText()
        stringTotal = name + "_" + mobileNo + "_" + doctorId + "_" + passw
        doctorInfo = open("doctorInfo.txt","w")
        doctorInfo.write(stringTotal)
        doctorInfo.close()
        os.system("python3 loginpage.py")

        


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "M-CARD"))
        self.welcometomcard.setText(_translate("Dialog", "WELCOME TO M-CARD"))
        self.nameField.setPlaceholderText(_translate("Dialog", "Enter Name"))
        self.mobileNoField.setPlaceholderText(_translate("Dialog", "Enter Mobile No"))
        self.doctorId.setPlaceholderText(_translate("Dialog", "Enter Doctor Id"))
        self.password.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.createaccount.setText(_translate("Dialog", "CREATE ACCOUNT"))
        self.medicard2020.setText(_translate("Dialog", "@M-CARD 2020"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
