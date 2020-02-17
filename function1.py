# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import urllib
import speech_recognition as sr
import time

def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


    

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
        
        self.pushButton.clicked.connect(self.speech)
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 320, 601, 231))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 290, 141, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 110, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 220, 241, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 180, 251, 31))
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
        self.pushButton_2.setText(_translate("Function", "Clear"))
        self.label_5.setText(_translate("Function", "TextLabel"))
        
    def speech(self):
        if connected():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                self.label_5.setText("Listening...")
                self.label_5.adjustSize()
                time.sleep(1)
    # read the audio data from the default microphone
                audio_data = r.listen(source,timeout=5)
                self.label_5.setText("Time over")
                time.sleep(1)
                self.label_5.setText("Recognizing...")
                time.sleep(1)
    # convert speech to text
                text = r.recognize_google(audio_data ,language='en-UK', show_all=True)
                try:
                    self.label_5.setText("You said:" )
                    list1=[]
                    self.comboBox.clear()
                    if (len(text)>0):
                        print(len(text["alternative"]))
                        for x in range(0,len(text["alternative"])):
                            list1.append(text["alternative"][x]["transcript"])
                        self.comboBox.addItems(list1)
                    
                    else:
                        time.sleep(1)
                        self.label_5.setText("\tNothing")
                except LookupError:
                    time.sleep(1)
                    self.label_5.setText("Could not Understand Value")

                except sr.UnknownValueError:
                    time.sleep(1)
                    self.label_5.setText("Voice Recognition could not understand audio")

                except sr.RequestError as e:
                    time.sleep(1)
                    self.label_5.setText("Voice Recognition could not request results ; {0}".format(e))
        else:
            time.sleep(1)
            self.label_5.setText("NO Internet Connection. \nCheck your Internet Connection")
        time.sleep(1)
        self.label_5.setText("Completed")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Function = QtWidgets.QMainWindow()
    ui = Ui_Function()
    ui.setupUi(Function)
    Function.show()
    sys.exit(app.exec_())

