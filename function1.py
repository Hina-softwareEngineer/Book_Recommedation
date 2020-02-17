# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Function(object):
    def setupUi(self, Function):
        Function.setObjectName("Function")
        Function.resize(737, 600)
        self.centralwidget = QtWidgets.QWidget(Function)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 70, 601, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 151, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 120, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 251, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 180, 101, 25))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 280, 621, 271))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 246, 141, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 110, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        Function.setCentralWidget(self.centralwidget)

        self.retranslateUi(Function)
        QtCore.QMetaObject.connectSlotsByName(Function)

    def retranslateUi(self, Function):
        _translate = QtCore.QCoreApplication.translate
        Function.setWindowTitle(_translate("Function", "MainWindow"))
        self.label.setText(_translate("Function", "Enter the Book Name:"))
        self.label_2.setText(_translate("Function", "OR"))
        self.label_3.setText(_translate("Function", "Write the Book Name by your Voice:"))
        self.pushButton.setText(_translate("Function", "Click and Say"))
        self.label_4.setText(_translate("Function", "Recommendations:"))
        self.pushButton_2.setText(_translate("Function", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Function = QtWidgets.QMainWindow()
    ui = Ui_Function()
    ui.setupUi(Function)
    Function.show()
    sys.exit(app.exec_())

