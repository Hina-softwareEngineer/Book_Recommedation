# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_welcome(object):
    def setupUi(self, welcome):
        welcome.setObjectName("welcome")
        welcome.resize(739, 600)
        welcome.setStyleSheet("Background-color: #696969;")
        self.centralwidget = QtWidgets.QWidget(welcome)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 90, 601, 61))
        self.label.setStyleSheet("\n"
"font-family: Lucida Console;\n"
"font-size: 25px;\n"
"font-weight: bold;\n"
"font-style: italic;\n"
"color: #ffffff;\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 250, 281, 71))
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: #ffffff;\n"
"background-color: #ff6347;\n"
"Border-radius: 30px;\n"
"font-size:30px\n"
"}\n"
"QPushButton:hover{\n"
"color: #ffffff;\n"
"background-color: #ff6347;\n"
"Border-radius: 30px;\n"
"background-color: #ff4500;\n"
"font-weight: bold;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        welcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(welcome)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        _translate = QtCore.QCoreApplication.translate
        welcome.setWindowTitle(_translate("welcome", "MainWindow"))
        self.label.setText(_translate("welcome", "Welcome To Book Recommendation System"))
        self.pushButton.setText(_translate("welcome", "Let\'s get started"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome = QtWidgets.QMainWindow()
    ui = Ui_welcome()
    ui.setupUi(welcome)
    welcome.show()
    sys.exit(app.exec_())

