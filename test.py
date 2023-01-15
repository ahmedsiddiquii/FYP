import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from  PyQt5.QtCore import *
from  PyQt5.QtGui import *
from  PyQt5.QtWidgets import *
import os
import sys
# from seleniumwire import webdriver
import subprocess
from PyQt5.QtWidgets import QMessageBox
import threading
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import random
from PyQt5.QtGui import QMovie
import icons_rc

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

stylesheet=open("style.txt","r").read()
class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login Page')
        self.setWindowIcon(QIcon('icon.png'))

        username_label = QLabel('Username:', self)
        username_label.move(50, 50)

        self.username_edit = QLineEdit(self)
        self.username_edit.move(150, 50)

        password_label = QLabel('Password:', self)
        password_label.move(50, 100)

        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.move(150, 100)

        login_button = QPushButton('Login', self)
        login_button.move(150, 150)

        self.setGeometry(300, 300, 300, 200)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.check_credentials()

    def check_credentials(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        if username == 'admin' and password == 'password':
            self.accept()
        else:
            self.username_edit.setText('')
            self.password_edit.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.setStyleSheet(stylesheet)
    login_page.show()
    sys.exit(app.exec_())

