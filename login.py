"""
File   :  login.py
Author :  Omer Golan & Omer Shtresler
Date   :  19/12/2020
Class  :  Yod-3
Created by: PyQt5 UI code generator 5.15.1
this is the code for the GUI of the login page
"""

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from MLProject.mainUI import Ui_MainWindow1
import tempfile

bol = False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        creates the GUI of the login page
        :param MainWindow:
        :return: the login window
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        MainWindow.setWindowTitle("")
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userName_L = QtWidgets.QLineEdit(self.centralwidget)
        self.userName_L.setGeometry(QtCore.QRect(50, 180, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userName_L.setFont(font)
        self.userName_L.setObjectName("userName_L")
        self.password_L = QtWidgets.QLineEdit(self.centralwidget)
        self.password_L.setGeometry(QtCore.QRect(50, 280, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_L.setFont(font)
        self.password_L.setObjectName("password_L")
        self.password_L.setEchoMode(2)
        self.lbl_Username_L = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Username_L.setGeometry(QtCore.QRect(50, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Username_L.setFont(font)
        self.lbl_Username_L.setObjectName("lbl_Username_L")
        self.lbl_Password_L = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Password_L.setGeometry(QtCore.QRect(50, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Password_L.setFont(font)
        self.lbl_Password_L.setObjectName("lbl_Password_L")
        self.lbl_Password_R = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Password_R.setGeometry(QtCore.QRect(490, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Password_R.setFont(font)
        self.lbl_Password_R.setObjectName("lbl_Password_R")
        self.password_R = QtWidgets.QLineEdit(self.centralwidget)
        self.password_R.setGeometry(QtCore.QRect(490, 280, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_R.setFont(font)
        self.password_R.setObjectName("password_R")
        self.password_R.setEchoMode(2)
        self.userName_R = QtWidgets.QLineEdit(self.centralwidget)
        self.userName_R.setGeometry(QtCore.QRect(490, 180, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userName_R.setFont(font)
        self.userName_R.setObjectName("userName_R")
        self.lbl_Username_R = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Username_R.setGeometry(QtCore.QRect(490, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Username_R.setFont(font)
        self.lbl_Username_R.setObjectName("lbl_Username_R")
        self.lbl_Register = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Register.setGeometry(QtCore.QRect(490, 40, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_Register.setFont(font)
        self.lbl_Register.setObjectName("lbl_Register")
        self.lbl_login = QtWidgets.QLabel(self.centralwidget)
        self.lbl_login.setGeometry(QtCore.QRect(50, 40, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_login.setFont(font)
        self.lbl_login.setObjectName("lbl_login")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(114, 350, 121, 41))
        self.btn_login.setObjectName("btn_login")
        self.btn_Register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Register.setGeometry(QtCore.QRect(554, 350, 121, 41))
        self.btn_Register.setObjectName("btn_Register")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, 0, 71, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # sets the login part of the page to be disabled
        self.btn_login.setDisabled(True)
        self.password_L.setDisabled(True)
        self.userName_L.setDisabled(True)
        # if the file exists sets the register part of the page to be disabled and the login part to be enabled
        if os.path.isfile(tempfile.gettempdir() + r"\temp.temp"):
            self.btn_Register.setDisabled(True)
            self.password_R.setDisabled(True)
            self.userName_R.setDisabled(True)

            self.btn_login.setDisabled(False)
            self.password_L.setDisabled(False)
            self.userName_L.setDisabled(False)

    def retranslateUi(self, MainWindow):
        """

        :param MainWindow:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        self.lbl_Username_L.setText(_translate("MainWindow", "Username:"))
        self.lbl_Password_L.setText(_translate("MainWindow", "Password:"))
        self.lbl_Password_R.setText(_translate("MainWindow", "Password:"))
        self.lbl_Username_R.setText(_translate("MainWindow", "Username:"))
        self.lbl_Register.setText(_translate("MainWindow", "Register:"))
        self.lbl_login.setText(_translate("MainWindow", "Login:"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.btn_Register.setText(_translate("MainWindow", "Register"))
        # connects the buttons to their respective functions
        self.btn_Register.clicked.connect(self.registerClicked)
        self.btn_login.clicked.connect(self.loginClicked)

    def registerClicked(self):
        """
        creates a file and writes the username and the password encrypted
        :return: a file with the username and the password encrypted
        """
        with open(tempfile.gettempdir() + r"\temp.temp", 'w') as f:
            f.write(self.encryptD("dragon", self.userName_R.text()))
            f.write('\n')
            f.write(self.encryptD("unicorn", self.password_R.text()))
            os.system("attrib +h +s +r " + tempfile.gettempdir() + r"\temp.temp")
        self.btn_Register.setDisabled(True)
        self.password_R.setDisabled(True)
        self.userName_R.setDisabled(True)

        self.btn_login.setDisabled(False)
        self.password_L.setDisabled(False)
        self.userName_L.setDisabled(False)

    def loginClicked(self):
        """
        checks the username and the password. and closes the window accordingly
        :return:
        """
        global bol
        with open(tempfile.gettempdir() + r"\temp.temp") as f:
            self.data = f.readlines()
            self.Username = self.data[0].rstrip()
            self.password = self.data[1].rstrip()

        if self.encryptD("dragon", self.userName_L.text()) == self.Username and self.encryptD("unicorn",
                                                                                              self.password_L.text()) == self.password:
            bol = True
            MainWindow.close()

    def f1(self, s1, s2):
        """
        encrypts/decrypts the flag with the key (xor)
        :param s1: key
        :param s2: flag
        :return: encrypted/decrypted string
        """
        return ''.join(chr(ord(x1) ^ ord(x2)) for x1, x2 in zip(s1, s2))

    def f2(self, s, x):
        """
        duplicates the string 'x' times
        :param s: string
        :param x: int
        :return: duplicated string
        """
        return (s * (int(x / len(s)) + x))[:x]

    def encryptD(self, key, flag):
        """
        encrypts/decrypts the username/password
        :param key: string to xor flag with
        :param flag: username/password
        :return: encrypted/decrypted username/password
        """
        return self.f1(flag, self.f2(key, len(flag)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

    if bol:
        x = Ui_MainWindow1()
        x.start()
