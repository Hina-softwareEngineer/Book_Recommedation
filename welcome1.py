# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from function1 import Ui_Function
import time

class Ui_welcome(object):
    def openwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Function()
        self.ui.setupUi(self.window)
#         time.sleep(5)
        self.window.show()
#         welcome.hide()
        
    def setupUi(self, welcome):
        welcome.setObjectName("welcome")
        welcome.resize(739, 600)
        self.centralwidget = QtWidgets.QWidget(welcome)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 230, 311, 71))
        self.label.setObjectName("label")
        welcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(welcome)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        _translate = QtCore.QCoreApplication.translate
        welcome.setWindowTitle(_translate("welcome", "MainWindow"))
        self.label.setText(_translate("welcome", "Welcome To Book Recommendation System"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome = QtWidgets.QMainWindow()
    ui = Ui_welcome()
    ui.setupUi(welcome)
    welcome.show()
    sys.exit(app.exec_())
