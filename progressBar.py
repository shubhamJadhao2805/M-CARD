# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressBar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
    
import time
import threading
import sys

TIME_LIMIT = 50
class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        for i in range(0,3):
            while count < TIME_LIMIT:
                count +=1
                time.sleep(0.05)
                self.countChanged.emit(count)
            count = 0
            self.countChanged.emit(count)
        exit()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(255, 104)
        Form.setStyleSheet("background-color:rgb(33, 33, 35)")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 10, 211, 61))
        self.progressBar.setStyleSheet("color:rgb(252, 20, 30)")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 70, 101, 16))
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.progressBar.setMaximum(50)
        self.progressBar.setValue(0)
        self.onButtonClick()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Please Wait..."))
    def onButtonClick(self):
        self.progressBar.setValue(0)
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()
        # self.count = self.count + 1
    def onCountChanged(self, value):
        self.progressBar.setValue(value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
