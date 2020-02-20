# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Function(object):
    def setupUi(self, Function):
        Function.setObjectName("Function")
        Function.resize(737, 600)
        Function.setStyleSheet("Background-color: #696969;")
        self.centralwidget = QtWidgets.QWidget(Function)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 70, 601, 31))
        self.lineEdit.setStyleSheet("color: #ffffff")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 191, 17))
        self.label.setStyleSheet("QLabel{\n"
"color: #ffffff;\n"
"font-family: Lucida Console;\n"
"font-size: 15px;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 120, 67, 17))
        self.label_2.setStyleSheet("QLabel{\n"
"color: #ffffff;\n"
"font-family: Lucida Console;\n"
"font-size: 20px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 311, 21))
        self.label_3.setStyleSheet("QLabel{\n"
"color: #ffffff;\n"
"font-family: Lucida Console;\n"
"font-size: 15px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 180, 121, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: #ffffff;\n"
"background-color: #ff6347;\n"
"Border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color: #ffffff;\n"
"background-color: #ff6347;\n"
"Border-radius: 10px;\n"
"background-color: #ff4500;\n"
"font-weight:bold;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 320, 601, 231))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"Background-color: #ffffff;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 290, 141, 21))
        self.label_4.setStyleSheet("QLabel{\n"
"color: #ffffff;\n"
"font-family: Lucida Console;\n"
"font-size: 15px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(538, 110, 111, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: #ffffff;\n"
"background-color: #ff6347;\n"
"Border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"color: #ffffff;\n"
"Background-color: #ff6347;\n"
"Border-radius: 10px;\n"
"background-color: #ff4500;\n"
"font-weight: bold;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 230, 241, 21))
        self.label_5.setStyleSheet("QLabel{\n"
"color: #ffffff;\n"
"font-family: Lucida Console;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(410, 170, 251, 31))
        self.comboBox.setStyleSheet("QcomboBox{\n"
"color: #ffffff;\n"
"Background-color: #ffffff;\n"
"font-family: Lucida Console;\n"
"}")
        self.comboBox.setObjectName("comboBox")
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
        self.pushButton_2.setText(_translate("Function", "Search"))
        self.label_5.setText(_translate("Function", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Function = QtWidgets.QMainWindow()
    ui = Ui_Function()
    ui.setupUi(Function)
    Function.show()
    sys.exit(app.exec_())

