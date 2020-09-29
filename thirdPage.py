# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirdPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import functools
from firebase import firebase
import sys
firebase = firebase.FirebaseApplication('https://m-card-2ac54.firebaseio.com/', None)

a = sys.argv[1:]
name = a[0][1:]
mobileNo = a[1]
idSelected  = a[2]


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 900)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color:rgb(0, 17, 31)")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(1040, 120, 321, 621))
        self.frame.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 40, 131, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/Users/shubhamjadhao/Desktop/CURRENT PROJECT/Akshay Projeact/PYTHON/icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 190, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(40, 120, 971, 621))
        self.frame_2.setStyleSheet("background-color:rgb(8, 34, 57)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 931, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 30, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(146, 35, 146)")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(160, 30, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 750, 151, 16))
        self.label_7.setStyleSheet("color:rgb(205, 208, 208)")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        datesInfo = firebase.get("/Users/" + idSelected[:-2] + "/Dates",None)
        self.array = list(datesInfo.values())


        count = 0
        for x in range(4):
            for y in range(4):
                if count < len(self.array):
                    self.nameLabel = QtWidgets.QLabel()
                    self.nameLabel.setStyleSheet("background-color:rgb(255, 255, 255)")
                    self.nameLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                    self.nameLabel.setText(self.array[count].upper())
                    self.nameLabel.setFrameShape(QtWidgets.QFrame.Box)
                    self.nameLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    self.nameLabel.mousePressEvent = functools.partial(self.prescriptionCLickedMethod,source_object=count)
                else:
                    self.nameLabel = QtWidgets.QLabel()
                count = count + 1
                self.gridLayout.addWidget(self.nameLabel, x, y)

    def prescriptionCLickedMethod(self,event,source_object):
    
        prescriptionInfo = firebase.get("/Users/" + idSelected[:-2] + "/" + self.array[source_object],None)
        arrayList = list(prescriptionInfo)
        print(prescriptionInfo)
        presDetailed = ""
        for i in range(2,len(arrayList)):
            string2 = str(arrayList[i]).split("_")
            name = string2[0]
            time = string2[1]
            quantity = string2[2]
            finalString = "Name = " + name + "\n" + "Time = " + time + "\n" + "Quantity = " + quantity + "\n" + "-----------------------------------------------------" 

            presDetailed = presDetailed + finalString

        prescriptionDetailsMessageBox = QtWidgets.QMessageBox()
        prescriptionDetailsMessageBox.setWindowTitle("PRESCRIPTION DETAILS")
        prescriptionDetailsMessageBox.setText("This is prescrption")
        prescriptionDetailsMessageBox.setIcon(QtWidgets.QMessageBox.Information)
        prescriptionDetailsMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.Save)
        prescriptionDetailsMessageBox.setDetailedText(presDetailed)
        prescriptionDetailsMessageBox.setInformativeText(arrayList[1])
        x = prescriptionDetailsMessageBox.exec()
        print(source_object)

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", name))
        self.label_6.setText(_translate("Dialog", "MEDI-"))
        self.label_5.setText(_translate("Dialog", "CARD"))
        self.label_7.setText(_translate("Dialog", "@ MEDICARD LTD 2020"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
