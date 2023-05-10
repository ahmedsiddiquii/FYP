import json

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
from API import *
from DataModel.healthCare import data
from QueryGenerator import *
import json

count = 0
domain_name = "hospitalManagement"
direction = None
data_list = []
back_exist=False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 634)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.472906, y1:0, x2:0.517241, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border:none;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_51.setContentsMargins(0, 12, 0, 30)
        self.verticalLayout_51.setSpacing(30)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.frame_84 = QtWidgets.QFrame(self.frame_6)
        self.frame_84.setMinimumSize(QtCore.QSize(80, 60))
        self.frame_84.setMaximumSize(QtCore.QSize(80, 60))
        self.frame_84.setStyleSheet("background:transparent;\n"
"border:none;")
        self.frame_84.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_84.setObjectName("frame_84")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.frame_84)
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.label_36 = QtWidgets.QLabel(self.frame_84)
        self.label_36.setStyleSheet("background:transparent;\n"
"image: url(:/all_icons/icons/3942534.png);")
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.verticalLayout_57.addWidget(self.label_36)
        self.verticalLayout_51.addWidget(self.frame_84)
        self.frame_83 = QtWidgets.QFrame(self.frame_6)
        self.frame_83.setStyleSheet("background:transparent;")
        self.frame_83.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_83.setObjectName("frame_83")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.frame_83)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setSpacing(30)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_83)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet("background:transparent;\n"
"qproperty-icon: url(:/all_icons/icons/icons8-home-page-48.png);\n"
"qproperty-iconSize: 50px;")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_55.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_83)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet("background:transparent;\n"
"qproperty-icon: url(:/all_icons/icons/icons8-setting-64.png);\n"
"qproperty-iconSize: 40px;")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_55.addWidget(self.pushButton_18)
        self.verticalLayout_51.addWidget(self.frame_83, 0, QtCore.Qt.AlignTop)
        self.frame_85 = QtWidgets.QFrame(self.frame_6)
        self.frame_85.setStyleSheet("background:transparent;")
        self.frame_85.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_85.setObjectName("frame_85")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.frame_85)
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_85)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet("background:transparent;\n"
"qproperty-icon: url(:/all_icons/icons/icons8-logout-64.png);\n"
"qproperty-iconSize: 40px;")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_56.addWidget(self.pushButton_19)
        self.verticalLayout_51.addWidget(self.frame_85, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("border:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_56 = QtWidgets.QFrame(self.frame)
        self.frame_56.setMinimumSize(QtCore.QSize(0, 72))
        self.frame_56.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(".Aqua Kana")
        self.frame_56.setFont(font)
        self.frame_56.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.625, x2:1, y2:0.494318, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border:none;")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_56)
        self.horizontalLayout_35.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_35 = QtWidgets.QLabel(self.frame_56)
        self.label_35.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_35.addWidget(self.label_35)
        self.label_22 = QtWidgets.QLabel(self.frame_56)
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:transparent;")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_35.addWidget(self.label_22)
        self.frame_57 = QtWidgets.QFrame(self.frame_56)
        self.frame_57.setStyleSheet("background:transparent;")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.horizontalLayout_35.addWidget(self.frame_57)
        self.verticalLayout_24.addWidget(self.frame_56)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setSizeIncrement(QtCore.QSize(0, 500))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_69 = QtWidgets.QFrame(self.frame_2)
        self.frame_69.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_69)
        self.verticalLayout_39.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_39.setSpacing(30)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.label_26 = QtWidgets.QLabel(self.frame_69)
        self.label_26.setMinimumSize(QtCore.QSize(450, 80))
        self.label_26.setMaximumSize(QtCore.QSize(450, 80))
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        font.setPointSize(37)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_39.addWidget(self.label_26, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.frame_69)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_39.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.frame_69)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(400, 440))
        self.frame_3.setMaximumSize(QtCore.QSize(400, 400))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setMinimumSize(QtCore.QSize(150, 100))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_7.setStyleSheet("image: url(:/all_icons/icons/3237472.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 12)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_15 = QtWidgets.QFrame(self.page_7)
        self.frame_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_11 = QtWidgets.QFrame(self.frame_15)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_11.setStyleSheet("border:none;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_26.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_26.setSpacing(30)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setMinimumSize(QtCore.QSize(801, 71))
        self.label_6.setMaximumSize(QtCore.QSize(801, 71))
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        font.setPointSize(37)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_26.addWidget(self.label_6)
        self.verticalLayout_9.addWidget(self.frame_11, 0, QtCore.Qt.AlignHCenter)
        self.frame_58 = QtWidgets.QFrame(self.frame_15)
        self.frame_58.setMinimumSize(QtCore.QSize(500, 391))
        self.frame_58.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_58.setStyleSheet("border:none;")
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_58)
        self.verticalLayout_25.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_25.setSpacing(30)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_16 = QtWidgets.QFrame(self.frame_58)
        self.frame_16.setMinimumSize(QtCore.QSize(401, 331))
        self.frame_16.setMaximumSize(QtCore.QSize(401, 331))
        self.frame_16.setStyleSheet("\n"
"border:none;\n"
"border-radius:6px;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 240, 401, 90))
        self.pushButton_8.setMinimumSize(QtCore.QSize(350, 80))
        self.pushButton_8.setMaximumSize(QtCore.QSize(401, 90))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
" border-radius: 6px;\n"
"image:none;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_27 = QtWidgets.QLabel(self.frame_16)
        self.label_27.setGeometry(QtCore.QRect(12, 12, 377, 212))
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_25.addWidget(self.frame_16, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_9.addWidget(self.frame_58, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.frame_15)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.frame_59 = QtWidgets.QFrame(self.page_8)
        self.frame_59.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_59.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.frame_59.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_59.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_59)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_60 = QtWidgets.QFrame(self.frame_59)
        self.frame_60.setMinimumSize(QtCore.QSize(291, 120))
        self.frame_60.setMaximumSize(QtCore.QSize(123177, 120))
        self.frame_60.setStyleSheet("border:none;")
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_60)
        self.verticalLayout_11.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_23 = QtWidgets.QLabel(self.frame_60)
        self.label_23.setMinimumSize(QtCore.QSize(0, 0))
        self.label_23.setMaximumSize(QtCore.QSize(1621777, 60))
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"padding:6px;")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_11.addWidget(self.label_23)
        self.verticalLayout_15.addWidget(self.frame_60)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_61 = QtWidgets.QScrollArea(self.frame_59)
        self.frame_61.setWidgetResizable(True)
        self.frame_61.setObjectName("frame_61")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 724, 243))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_24.setMinimumSize(QtCore.QSize(700, 0))
        self.label_24.setMaximumSize(QtCore.QSize(700, 400))
        font = QtGui.QFont()
        font.setFamily("Apple Color Emoji")
        font.setPointSize(18)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("\n"
"border-radius:8px;\n"
"\n"
"color: rgb(76, 76, 76);\n"
"")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_14.addWidget(self.label_24)
        self.frame_61.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.addWidget(self.frame_61, 0, 0, 1, 1)
        self.verticalLayout_15.addLayout(self.gridLayout_2)
        self.frame_62 = QtWidgets.QFrame(self.frame_59)
        self.frame_62.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_62.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_62)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_62)
        self.pushButton_9.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_9.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_7.addWidget(self.pushButton_9, 0, QtCore.Qt.AlignLeft)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_62)
        self.pushButton_10.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_10.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("\n"
"border-radius:20px;\n"
"\n"
"qproperty-icon: url(:/all_icons/icons/7945189.png);\n"
"qproperty-iconSize: 40px;\n"
"border:none;\n"
"color: rgb(0, 0, 0);")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_15.addWidget(self.frame_62)
        self.verticalLayout_28.addWidget(self.frame_59)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.frame_65 = QtWidgets.QFrame(self.page_9)
        self.frame_65.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_65.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_65.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_65)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_63 = QtWidgets.QFrame(self.frame_65)
        self.frame_63.setMinimumSize(QtCore.QSize(291, 120))
        self.frame_63.setMaximumSize(QtCore.QSize(123177, 120))
        self.frame_63.setStyleSheet("border:none;")
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_63)
        self.verticalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_25 = QtWidgets.QLabel(self.frame_63)
        self.label_25.setMinimumSize(QtCore.QSize(0, 0))
        self.label_25.setMaximumSize(QtCore.QSize(1621777, 60))
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_12.addWidget(self.label_25)
        self.verticalLayout_18.addWidget(self.frame_63)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_70 = QtWidgets.QFrame(self.frame_65)
        self.frame_70.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_70.setStyleSheet("padding:10px;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_70.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_70)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_70)
        self.checkBox_3.setMaximumSize(QtCore.QSize(3533533, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_3.setStyleSheet("color: rgb(70, 70, 70);\n"
"")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_37.addWidget(self.checkBox_3, 0, QtCore.Qt.AlignTop)
        self.gridLayout_3.addWidget(self.frame_70, 0, 0, 1, 1)
        self.verticalLayout_18.addLayout(self.gridLayout_3)
        self.frame_66 = QtWidgets.QFrame(self.frame_65)
        self.frame_66.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_66.setMaximumSize(QtCore.QSize(16777215, 74))
        self.frame_66.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_66)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_66)
        self.pushButton_11.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_11.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_16.addWidget(self.pushButton_11, 0, QtCore.Qt.AlignLeft)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_66)
        self.pushButton_12.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_12.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("\n"
"border-radius:20px;\n"
"\n"
"qproperty-icon: url(:/all_icons/icons/7945189.png);\n"
"qproperty-iconSize: 40px;\n"
"\n"
"color: rgb(0, 0, 0);")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_16.addWidget(self.pushButton_12, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_18.addWidget(self.frame_66)
        self.verticalLayout_35.addWidget(self.frame_65)
        self.stackedWidget.addWidget(self.page_9)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(self.page_2)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:transparent;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(548, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(1621775, 1621775))
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"QScrollBar\n"
"{\n"
"background : rgb(243, 243, 243);\n"
"};\n"
"QScrollBar::handle\n"
"{\n"
"background : rgb(70, 144, 255)\n"
"};\n"
"QScrollBar::handle::pressed\n"
"{\n"
"background : rgb(68, 100, 255);\n"
"};")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_8)
        self.scrollArea.setStyleSheet("QScrollBar\n"
"{\n"
"background : rgb(243, 243, 243);}\n"
"QScrollBar::handle\n"
"{\n"
"background : rgb(70, 144, 255);\n"
"}\n"
"QScrollBar::handle::pressed\n"
"{\n"
"background : rgb(68, 100, 255);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 374, 177))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(350, 1621777))
        self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_12.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.488, y1:0, x2:0.497537, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:transparent;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.frame_12)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_10)
        self.scrollArea_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"QScrollBar\n"
"{\n"
"background : qlineargradient(spread:pad, x1:0.477833, y1:0.0170455, x2:0.463054, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(232, 232, 232, 255));\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background : qlineargradient(spread:pad, x1:0.488, y1:0, x2:0.497537, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"}\n"
"QScrollBar::handle::pressed\n"
"{\n"
"background : rgb(68, 100, 255);\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 136, 124))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_13.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.verticalLayout_8.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_14.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_6.addWidget(self.checkBox_2)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.addWidget(self.scrollArea_2)
        self.gridLayout.addWidget(self.frame_10, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.page_2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 85))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignLeft)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("\n"
"border-radius:20px;\n"
"\n"
"qproperty-icon: url(:/all_icons/icons/7945189.png);\n"
"qproperty-iconSize: 40px;\n"
"\n"
"color: rgb(0, 0, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_9)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_16.setContentsMargins(30, 10, 30, 20)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_20 = QtWidgets.QFrame(self.page_3)
        self.frame_20.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_20.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background:transparent;")
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.verticalLayout_16.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.page_3)
        self.frame_21.setMinimumSize(QtCore.QSize(200, 100))
        self.frame_21.setMaximumSize(QtCore.QSize(1621777, 1621777))
        self.frame_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.scrollArea_4 = QtWidgets.QFrame(self.frame_21)
        self.scrollArea_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollArea_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.scrollArea_4)
        self.comboBox_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_2.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_4.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.scrollArea_4)
        self.comboBox_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox_3.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_4.addWidget(self.comboBox_3, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollArea_4)
        self.label_12.setMinimumSize(QtCore.QSize(0, 25))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_12.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"")
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.scrollArea_4)
        self.comboBox_4.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_4.addWidget(self.comboBox_4, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollArea_4)
        self.label_10.setMinimumSize(QtCore.QSize(0, 20))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_10.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"")
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollArea_4)
        self.label_11.setMinimumSize(QtCore.QSize(0, 25))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_11.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"")
        self.label_11.setMidLineWidth(20)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.scrollArea_4)
        self.scrollArea_5 = QtWidgets.QFrame(self.frame_21)
        self.scrollArea_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollArea_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.scrollArea_5)
        self.comboBox_6.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_5.addWidget(self.comboBox_6, 3, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.scrollArea_5)
        self.comboBox_5.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_5.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_5.addWidget(self.comboBox_5, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollArea_5)
        self.label_13.setMinimumSize(QtCore.QSize(0, 25))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"")
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.scrollArea_5)
        self.comboBox_7.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_5.addWidget(self.comboBox_7, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollArea_5)
        self.label_16.setMinimumSize(QtCore.QSize(0, 25))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_16.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"")
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollArea_5)
        self.label_15.setMinimumSize(QtCore.QSize(0, 25))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_15.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"")
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.scrollArea_5)
        self.scrollArea_6 = QtWidgets.QFrame(self.frame_21)
        self.scrollArea_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollArea_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_18 = QtWidgets.QLabel(self.scrollArea_6)
        self.label_18.setMinimumSize(QtCore.QSize(0, 25))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_18.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"")
        self.label_18.setMidLineWidth(0)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 5, 0, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.scrollArea_6)
        self.comboBox_10.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_6.addWidget(self.comboBox_10, 1, 2, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.scrollArea_6)
        self.comboBox_8.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout_6.addWidget(self.comboBox_8, 5, 2, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.scrollArea_6)
        self.comboBox_9.setStyleSheet("\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_6.addWidget(self.comboBox_9, 6, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollArea_6)
        self.label_17.setMinimumSize(QtCore.QSize(0, 25))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_17.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"")
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 6, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollArea_6)
        self.label_20.setMinimumSize(QtCore.QSize(0, 25))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_20.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"")
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 1, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.scrollArea_6)
        self.verticalLayout_16.addWidget(self.frame_21)
        self.frame_19 = QtWidgets.QFrame(self.page_3)
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_41 = QtWidgets.QFrame(self.frame_19)
        self.frame_41.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_41.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_19 = QtWidgets.QLabel(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background:transparent;\n"
"")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_31.addWidget(self.label_19, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_13.addWidget(self.frame_41)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_19)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_13.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_19)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_13.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_19)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_13.addWidget(self.checkBox_6)
        self.verticalLayout_16.addWidget(self.frame_19)
        self.frame_31 = QtWidgets.QFrame(self.page_3)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_31.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_31.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_10.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignLeft)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_5.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border-radius:20px;\n"
"\n"
"qproperty-icon: url(:/all_icons/icons/7945189.png);\n"
"qproperty-iconSize: 40px;\n"
"\n"
"color: rgb(0, 0, 0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_10.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_16.addWidget(self.frame_31)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_23.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_23.setSpacing(30)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_45 = QtWidgets.QFrame(self.page_4)
        self.frame_45.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_45.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_45.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_45)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.label_14 = QtWidgets.QLabel(self.frame_45)
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background:transparent;\n"
"")
        self.label_14.setTextFormat(QtCore.Qt.PlainText)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_41.addWidget(self.label_14)
        self.verticalLayout_23.addWidget(self.frame_45)
        self.frame_46 = QtWidgets.QFrame(self.page_4)
        self.frame_46.setMinimumSize(QtCore.QSize(0, 320))
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_46)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.frame_47 = QtWidgets.QFrame(self.frame_46)
        self.frame_47.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_47)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_48 = QtWidgets.QFrame(self.frame_47)
        self.frame_48.setMinimumSize(QtCore.QSize(230, 0))
        self.frame_48.setMaximumSize(QtCore.QSize(230, 125))
        self.frame_48.setStyleSheet("border-radius:10px;")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_48)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_49 = QtWidgets.QFrame(self.frame_48)
        self.frame_49.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_49.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.frame_49)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_28 = QtWidgets.QLabel(self.frame_49)
        self.label_28.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background:transparent;")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_42.addWidget(self.label_28)
        self.verticalLayout_20.addWidget(self.frame_49)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_48)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_3.setStyleSheet("    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_20.addWidget(self.lineEdit_3)
        self.gridLayout_7.addWidget(self.frame_48, 0, 0, 1, 1)
        self.frame_79 = QtWidgets.QFrame(self.frame_47)
        self.frame_79.setMinimumSize(QtCore.QSize(230, 0))
        self.frame_79.setMaximumSize(QtCore.QSize(230, 125))
        self.frame_79.setStyleSheet("border-radius:10px;")
        self.frame_79.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_79.setObjectName("frame_79")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.frame_79)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.frame_76 = QtWidgets.QFrame(self.frame_79)
        self.frame_76.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_76.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_76.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_76.setObjectName("frame_76")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.frame_76)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.label_34 = QtWidgets.QLabel(self.frame_76)
        self.label_34.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background:transparent;")
        self.label_34.setObjectName("label_34")
        self.verticalLayout_48.addWidget(self.label_34)
        self.verticalLayout_49.addWidget(self.frame_76)
        self.comboBox = QtWidgets.QComboBox(self.frame_79)
        self.comboBox.setStyleSheet("    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout_49.addWidget(self.comboBox)
        self.gridLayout_7.addWidget(self.frame_79, 0, 1, 1, 1)
        self.frame_73 = QtWidgets.QFrame(self.frame_47)
        self.frame_73.setMinimumSize(QtCore.QSize(230, 0))
        self.frame_73.setMaximumSize(QtCore.QSize(230, 125))
        self.frame_73.setStyleSheet("border-radius:10px;")
        self.frame_73.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_73)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_50 = QtWidgets.QFrame(self.frame_73)
        self.frame_50.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_50.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_50)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.label_29 = QtWidgets.QLabel(self.frame_50)
        self.label_29.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background:transparent;")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_43.addWidget(self.label_29)
        self.verticalLayout_21.addWidget(self.frame_50)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_73)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_4.setStyleSheet("    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_21.addWidget(self.lineEdit_4)
        self.gridLayout_7.addWidget(self.frame_73, 0, 2, 1, 1)
        self.frame_78 = QtWidgets.QFrame(self.frame_47)
        self.frame_78.setMinimumSize(QtCore.QSize(230, 0))
        self.frame_78.setMaximumSize(QtCore.QSize(230, 125))
        self.frame_78.setStyleSheet("border-radius:10px;")
        self.frame_78.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_78.setObjectName("frame_78")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_78)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.frame_74 = QtWidgets.QFrame(self.frame_78)
        self.frame_74.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_74.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_74.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_74)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.label_32 = QtWidgets.QLabel(self.frame_74)
        self.label_32.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background:transparent;")
        self.label_32.setObjectName("label_32")
        self.verticalLayout_46.addWidget(self.label_32)
        self.verticalLayout_45.addWidget(self.frame_74)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_78)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_10.setStyleSheet("    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_45.addWidget(self.lineEdit_10)
        self.gridLayout_7.addWidget(self.frame_78, 1, 0, 1, 1)
        self.frame_80 = QtWidgets.QFrame(self.frame_47)
        self.frame_80.setMinimumSize(QtCore.QSize(230, 0))
        self.frame_80.setMaximumSize(QtCore.QSize(230, 125))
        self.frame_80.setStyleSheet("border-radius:10px;")
        self.frame_80.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_80.setObjectName("frame_80")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.frame_80)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.frame_75 = QtWidgets.QFrame(self.frame_80)
        self.frame_75.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_75.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_75.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.frame_75)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.label_33 = QtWidgets.QLabel(self.frame_75)
        self.label_33.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("background:transparent;")
        self.label_33.setObjectName("label_33")
        self.verticalLayout_47.addWidget(self.label_33)
        self.verticalLayout_50.addWidget(self.frame_75)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_80)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_11.setStyleSheet("    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_50.addWidget(self.lineEdit_11)
        self.gridLayout_7.addWidget(self.frame_80, 1, 1, 1, 1)
        self.frame_77 = QtWidgets.QFrame(self.frame_47)
        self.frame_77.setMinimumSize(QtCore.QSize(230, 0))
        self.frame_77.setMaximumSize(QtCore.QSize(230, 120))
        self.frame_77.setStyleSheet("border-radius:10px;")
        self.frame_77.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_77.setObjectName("frame_77")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_77)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_72 = QtWidgets.QFrame(self.frame_77)
        self.frame_72.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_72.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_72.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_72)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.label_30 = QtWidgets.QLabel(self.frame_72)
        self.label_30.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("background:transparent;")
        self.label_30.setObjectName("label_30")
        self.verticalLayout_44.addWidget(self.label_30)
        self.verticalLayout_34.addWidget(self.frame_72)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_77)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_6.setStyleSheet("    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border:1px solid rgb(70, 151, 255);\n"
" padding: 6px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_34.addWidget(self.lineEdit_6)
        self.gridLayout_7.addWidget(self.frame_77, 1, 2, 1, 1)
        self.horizontalLayout_34.addWidget(self.frame_47, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_23.addWidget(self.frame_46)
        self.frame_22 = QtWidgets.QFrame(self.page_4)
        self.frame_22.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_22.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_16.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_16.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_8.addWidget(self.pushButton_16, 0, QtCore.Qt.AlignLeft)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_6.setMinimumSize(QtCore.QSize(170, 50))
        self.pushButton_6.setMaximumSize(QtCore.QSize(170, 50))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.448276, y2:1, stop:0 rgba(243, 167, 73, 255), stop:1 rgba(232, 105, 30, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_8.addWidget(self.pushButton_6)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_13.setMinimumSize(QtCore.QSize(130, 35))
        self.pushButton_13.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_8.addWidget(self.pushButton_13)
        self.verticalLayout_23.addWidget(self.frame_22)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.frame_51 = QtWidgets.QFrame(self.page_5)
        self.frame_51.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_51.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_51.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_53.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_53.setSpacing(30)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.label_21 = QtWidgets.QLabel(self.frame_51)
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(37)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"padding:6px;\n"
"")
        self.label_21.setTextFormat(QtCore.Qt.PlainText)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_53.addWidget(self.label_21)
        self.label_9 = QtWidgets.QLabel(self.frame_51)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 150))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_53.addWidget(self.label_9)
        self.label_31 = QtWidgets.QLabel(self.frame_51)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.verticalLayout_53.addWidget(self.label_31, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_54.addWidget(self.frame_51)
        self.frame_53 = QtWidgets.QFrame(self.page_5)
        self.frame_53.setMinimumSize(QtCore.QSize(0, 130))
        self.frame_53.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_53.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_53)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_52 = QtWidgets.QFrame(self.frame_53)
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_52)
        self.horizontalLayout_15.setContentsMargins(30, 30, 30, 30)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_52)
        self.pushButton_14.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_14.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("color: rgb(86, 168, 255);\n"
"qproperty-icon: url(:/all_icons/icons/3031718.png);\n"
"qproperty-iconSize: 30px;\n"
"background-color: qlineargradient(spread:pad, x1:0.477833, y1:0.0170455, x2:0.463054, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(232, 232, 232, 255));\n"
"border-radius:6px;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_15.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_52)
        self.pushButton_15.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_15.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("color: rgb(89, 162, 171);\n"
"qproperty-icon: url(:/all_icons/icons/9261197.png);\n"
"qproperty-iconSize: 30px;\n"
"background-color: qlineargradient(spread:pad, x1:0.477833, y1:0.0170455, x2:0.463054, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(232, 232, 232, 255));\n"
"border-radius:6px;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_15.addWidget(self.pushButton_15)
        self.horizontalLayout_12.addWidget(self.frame_52)
        self.frame_54 = QtWidgets.QFrame(self.frame_53)
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_54)
        self.verticalLayout_22.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_54)
        self.pushButton_7.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_7.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("color:rgb(127, 193, 60);\n"
"qproperty-icon: url(:/all_icons/icons/4122925.png);\n"
"qproperty-iconSize: 30px;\n"
"background-color: qlineargradient(spread:pad, x1:0.477833, y1:0.0170455, x2:0.463054, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(232, 232, 232, 255));\n"
"border-radius:6px;\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_22.addWidget(self.pushButton_7)
        self.horizontalLayout_12.addWidget(self.frame_54, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_54.addWidget(self.frame_53)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.frame_55 = QtWidgets.QFrame(self.page_6)
        self.frame_55.setGeometry(QtCore.QRect(160, 80, 741, 581))
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_55)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(83, 127, 361, 261))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.stackedWidget.addWidget(self.page_6)
        self.verticalLayout_24.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">A</span><span style=\" font-size:24pt; font-weight:600;\">utomative</span><span style=\" font-size:36pt; font-weight:600;\">D</span><span style=\" font-size:24pt; font-weight:600;\">atabase</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "Automative Database"))
        self.label_2.setText(_translate("MainWindow", "Secure Login"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Forget password?"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label_6.setText(_translate("MainWindow", "Welcome Username"))
        self.pushButton_8.setText(_translate("MainWindow", "Start Wizard"))
        self.label_23.setText(_translate("MainWindow", "Documentation"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,serif\'; font-style:italic; color:#3f3f3f;\">o Select the Domain.</span></p><p><span style=\" font-family:\'Times New Roman,serif\'; font-style:italic; color:#3f3f3f;\">o Select the Sub-Model. </span></p><p><span style=\" font-family:\'Times New Roman,serif\'; font-style:italic; color:#3f3f3f;\">o Select the Attributes which You need. </span></p><p><span style=\" font-family:\'Times New Roman,serif\'; font-style:italic; color:#3f3f3f;\">o Select the Sytyling You want. </span></p><p><span style=\" font-family:\'Times New Roman,serif\'; font-style:italic; color:#3f3f3f;\">o Select the Output Category.</span></p><p><span style=\" font-family:\'Times New Roman,serif\'; font-style:italic; color:#3f3f3f;\">o Write the Database Connection.</span></p><p><span style=\" font-family:\'Times New Roman,serif\'; font-style:italic; color:#3f3f3f;\">o Click on the Generate Button.</span></p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Back"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">Select Domain</span></p></body></html>"))
        self.checkBox_3.setText(_translate("MainWindow", "Health and Care"))
        self.pushButton_11.setText(_translate("MainWindow", "Back"))
        self.label_4.setText(_translate("MainWindow", "Health Care Shipment &Delivery"))
        self.label_5.setText(_translate("MainWindow", "Health Care Delivery Role"))
        self.checkBox.setText(_translate("MainWindow", "From Date"))
        self.checkBox_2.setText(_translate("MainWindow", "Thru Date"))
        self.pushButton_2.setText(_translate("MainWindow", "Back"))
        self.label_8.setText(_translate("MainWindow", "Prototype|Preferences"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "Output"))
        self.checkBox_4.setText(_translate("MainWindow", "Generate SQl Queries"))
        self.checkBox_5.setText(_translate("MainWindow", "Generate Prototype"))
        self.checkBox_6.setText(_translate("MainWindow", "Save DB File"))
        self.pushButton_4.setText(_translate("MainWindow", "Back"))
        self.label_14.setText(_translate("MainWindow", "Database Connection"))
        self.label_28.setText(_translate("MainWindow", "Host"))
        self.label_34.setText(_translate("MainWindow", "Engine Name"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MYSQL"))
        self.label_29.setText(_translate("MainWindow", "Port"))
        self.label_32.setText(_translate("MainWindow", "Password"))
        self.label_33.setText(_translate("MainWindow", "Database"))
        self.label_30.setText(_translate("MainWindow", "Username"))
        self.pushButton_16.setText(_translate("MainWindow", "Back"))
        self.pushButton_6.setText(_translate("MainWindow", "Test Connection"))
        self.pushButton_13.setText(_translate("MainWindow", "Generate"))
        self.label_21.setText(_translate("MainWindow", "Process In Progress"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; color:#404040;\">Please Wait…</span></p><p><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; color:#404040;\">Stay connected with us while we are preparing your schema and prototype...</span></p><p><span style=\" font-family:\'Courier New\'; font-size:14pt; color:#404040;\">    o </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; color:#404040;\">Do not close the application until process finished.</span></p><p><span style=\" font-family:\'Courier New\'; font-size:14pt; color:#404040;\">    o </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; color:#404040;\">keep your internet conected if your database is on cloud.</span></p></body></html>"))
        self.pushButton_14.setText(_translate("MainWindow", "Download SQL File"))
        self.pushButton_15.setText(_translate("MainWindow", "Download ERD"))
        self.pushButton_7.setText(_translate("MainWindow", "Create New"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "IMAGE UML\n"
""))

    def create_screen(self):

        global count


        for i, value in enumerate(data['Domain']):
                domain = data["Domain"][value]
                # #print(domain)
                        # #print(direction)
                for j, entities in enumerate(domain):
                        self.label_4.setText(entities)
                                # #print(domain)
                        count += 1
                        print(count,"==count is")
                        yield self.create_cards(domain[entities])


        return

    def back_screen(self):

            global count,data_list
            key_value=""
            count -= 1

            print(count,"==count is")
            for t in data_list[count]:
                    key_value=t
                    break
            #print(data_list[count],"piaza2")
            self.label_4.setText(key_value)

            #print(data_list[count],"piaza")
            #print(key_value)
            return self.create_cards(data_list[count][key_value])
    def next_screen_normal(self):

            global count,data_list
            key_value=""
            count += 1

            print(count,"==count is")
            print(len(data_list))
            try:
                    for t in data_list[count]:
                            key_value=t
                            break
                    #print(data_list[count],"piaza2")
                    self.label_4.setText(key_value)

                    #print(data_list[count],"piaza")
                    #print(key_value)
                    return self.create_cards(data_list[count][key_value])
            except:
                    try:
                        next(self.create_screen())
                    except:
                        self.stackedWidget.setCurrentWidget(self.ui.page_4)

    def create_cards(self,domain):
            #print(domain)
            self.labels=[]
            for i,value in enumerate(domain):
                    # #print(value)
                    # data_list.append([temp])
                    entity = domain[value]

                    self.frame_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
                    self.frame_10.setMinimumSize(QtCore.QSize(520, 411))
                    self.frame_10.setMaximumSize(QtCore.QSize(1621777, 1621777))
                    self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "border-radius:9px;")
                    self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
                    shadow = QGraphicsDropShadowEffect(xOffset=1, yOffset=1)
                    shadow.setBlurRadius(20)
                    shadow.setColor(QtGui.QColor(200, 200, 200))
                    # adding shadow to the label
                    self.frame_10.setGraphicsEffect(shadow)
                    self.frame_10.setObjectName("frame_10")
                    self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
                    self.verticalLayout_7.setObjectName("verticalLayout_7")
                    self.frame_12 = QtWidgets.QFrame(self.frame_10)
                    self.frame_12.setMaximumSize(QtCore.QSize(600, 50))
                    # self.frame_12.setMinimumSize(QtCore.QSize(600, 60))
                    self.frame_12.setStyleSheet(
                            "background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
                            "color: rgb(255, 255, 255);\n"
                            "border-radius:10px;")
                    self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.frame_12.setObjectName("frame_12")
                    self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_12)
                    self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                    self.label_5 = QtWidgets.QLabel(self.frame_12)

                    font = QtGui.QFont()
                    font.setPointSize(18)
                    font.setBold(True)
                    font.setWeight(75)
                    self.label_5.setFont(font)
                    self.label_5.setObjectName("label_5")
                    self.label_5.setStyleSheet("background:transparent;")
                    self.label_5.setText(value)
                    self.labels.append(self.label_5)
                    # temp[self.label_4.text()][self.label_5.text()] = {}
                    # #print(value)

                    self.horizontalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
                    self.verticalLayout_7.addWidget(self.frame_12)
                    self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_10)
                    self.scrollArea_2.setStyleSheet(
                            "background-color: qlineargradient(spread:pad, x1:0.502463, y1:0, x2:0.527, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
                            "border-radius:10px;\n"
                            "QScrollBar\n"
                            "{\n"
                            "background : qlineargradient(spread:pad, x1:0.477833, y1:0.0170455, x2:0.463054, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(232, 232, 232, 255));\n"
                            "}\n"
                            "QScrollBar::handle\n"
                            "{\n"
                            "background : qlineargradient(spread:pad, x1:0.488, y1:0, x2:0.497537, y2:1, stop:0 rgba(55, 164, 255, 255), stop:1 rgba(71, 80, 246, 255));\n"
                            "width;20px;\n"
                            "}\n"
                            "QScrollBar::handle::pressed\n"
                            "{\n"
                            "background : rgb(68, 100, 255);\n"
                            "}")
                    self.scrollArea_2.setWidgetResizable(True)
                    self.scrollArea_2.setObjectName("scrollArea_2")
                    self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
                    self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 982, 451))
                    self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
                    self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
                    self.verticalLayout_8.setObjectName("verticalLayout_8")
                    temp_buttons=[]
                    for j,attribute in enumerate(entity):
                            self.frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
                            self.frame_13.setMaximumSize(QtCore.QSize(16777215, 50))
                            self.frame_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                        "color: rgb(0, 0, 0);")
                            self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
                            self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
                            self.frame_13.setObjectName("frame_13")
                            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_13)
                            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                            self.checkBox = QtWidgets.QCheckBox(self.frame_13)
                            self.checkBox.setObjectName("checkBox")
                            self.checkBox.setStyleSheet("background:transparent;\n"
                                                        "color: rgb(69, 69, 69);")
                            # #print(attribute)
                            # #print(entity[attribute])
                            self.checkBox.setText(attribute + f" : {entity[attribute]['data_type']}")
                            temp_buttons.append(self.checkBox)
                            # temp[self.label_4.text()][self.label_5.text()][self.checkBox.text()] = {}

                            try:
                                    if entity[attribute]['checkable']==False:
                                            self.checkBox.setDisabled(True)

                            except:
                                    pass
                            try:
                                    if entity[attribute]['checked'] == True:
                                            self.checkBox.setChecked(True)

                            except Exception as e:

                                    pass
                            self.horizontalLayout_5.addWidget(self.checkBox)
                            self.verticalLayout_8.addWidget(self.frame_13)
                    self.buttons.append(temp_buttons)
                    self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
                    self.verticalLayout_7.addWidget(self.scrollArea_2)
                    self.gridLayout.addWidget(self.frame_10, 0, i, 1, 1)
                    self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            # #print(temp)
            # #print(data_list)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowTitle('')
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.movie = QMovie("83426-database.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.movie2 = QMovie("icons/wizard2.gif")
        self.ui.label_27.setMovie(self.movie2)
        self.ui.pushButton_15.setDisabled(True)
        self.movie2.start()
        self.set_shadow()
        self.ui.frame_6.hide()
        self.ui.frame_56.hide()
        self.button_connection()
        initializeDB()
        self.screen_generator=self.ui.create_screen()
        # self.back_screen_generator=self.ui.back_screen()
        self.ui.buttons=[]
        self.ui.labels=[]
        self.ui.lineEdit_3.setText("localhost")
        self.ui.lineEdit_4.setText("3306")
        self.ui.lineEdit_10.setText("12345678")
        self.ui.lineEdit_6.setText("root")
    def call_dbscreen(self):
            #print("db screen")
            global data_list,domain_name
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
            with open("data_list.txt","w") as f:
                    jsonn={domain_name:data_list}
                    f.write(json.dumps(jsonn))
    def button_connection(self):
            self.ui.pushButton.clicked.connect(self.callAuth)
            self.ui.pushButton_8.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))
            self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_9))
            self.ui.pushButton_16.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
            self.ui.pushButton_13.clicked.connect(lambda: self.genrateDB())
            self.ui.pushButton_9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))
            self.ui.pushButton_11.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_8))
            self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
            self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
            self.ui.pushButton_7.clicked.connect(self.reset)
            self.ui.pushButton_12.clicked.connect(lambda: self.start_render())

            self.ui.pushButton_3.clicked.connect(lambda:self.call_next(True))

            self.ui.pushButton_2.clicked.connect(lambda: self.call_next(False))
    def reset(self):
            global count,domain_name,direction,data_list,back_exist
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_7)
            self.screen_generator = self.ui.create_screen()
            count = 0
            domain_name = "hospitalManagement"
            direction = None
            data_list = []
            back_exist = False
    def start_render(self):
            global count,back_exist
            if back_exist==False:
                next(self.screen_generator)

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            count=0
            # self.call_next(False)

    def set_shadow(self):
        shadow = QGraphicsDropShadowEffect(xOffset=1, yOffset=1)
        shadow.setBlurRadius(80)
        shadow.setColor(QtGui.QColor(200, 200, 200))
        # adding shadow to the label
        self.ui.frame_3.setGraphicsEffect(shadow)

        shadow2 = QGraphicsDropShadowEffect(xOffset=1, yOffset=1)
        shadow2.setBlurRadius(80)
        shadow2.setColor(QtGui.QColor(200, 200, 200))


        # adding shadow to the label
        self.ui.frame_16.setGraphicsEffect(shadow2)


        frames=[self.ui.label_26,self.ui.label_6,self.ui.label_23,self.ui.pushButton_9,self.ui.pushButton_10,self.ui.label_25,self.ui.frame_61,self.ui.frame_70,self.ui.label_25,self.ui.pushButton_11,
                self.ui.pushButton_12,self.ui.label_25,self.ui.frame_7,self.ui.page_2,self.ui.pushButton_3,self.ui.frame_20,self.ui.scrollArea_4,self.ui.scrollArea_5,
                self.ui.scrollArea_6,self.ui.frame_41,self.ui.pushButton_4,self.ui.pushButton_5,self.ui.frame_45,self.ui.frame_48,self.ui.frame_73,self.ui.frame_78,
                self.ui.frame_77,self.ui.frame_79,self.ui.frame_80,self.ui.pushButton_6,self.ui.pushButton_13,self.ui.label_21,self.ui.pushButton_14,self.ui.pushButton_15,self.ui.pushButton_7]
        for f in frames:
                shadow = QGraphicsDropShadowEffect(xOffset=1, yOffset=1)
                shadow.setBlurRadius(30)
                shadow.setColor(QtGui.QColor(190, 190, 190))
                # adding shadow to the label
                f.setGraphicsEffect(shadow)

    def callAuth(self):
        username = self.ui.lineEdit.text().casefold()
        password = self.ui.lineEdit_2.text()
        if auth(username,password) == True:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_7)
                self.ui.frame_6.show()
                self.ui.frame_56.show()
        else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Username or Password is wrong')
                msg.setWindowTitle("Error")
                msg.exec_()
    def genrateDB(self):
            username = self.ui.lineEdit_6.text()
            password = self.ui.lineEdit_10.text()
            host = self.ui.lineEdit_3.text()
            port = self.ui.lineEdit_4.text()
            dbname = self.ui.lineEdit_11.text()
            self.movie3 = QMovie("icons/97952-loading-animation-blue.gif")
            self.ui.label_31.setMovie(self.movie3)
            self.movie3.start()
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
            obj = QueryGenerator()
            print(obj.define_db_name())
            print(obj.define_entities())
            print(obj.define_sub_entities())
            print(username,password,host,port,dbname)
            obj.generate_sub_tables(username,password,host,port,dbname)
            obj.generate_main_tables(username,password,host,port,dbname)


            # self.movie3 = QMovie("icons/95775-done-blue.gif")
            # self.ui.label_31.setMovie(self.movie3)
            # self.movie3.start()
    def call_next(self, direction_temp):
            global count, domain_name, direction,data_list, back_exist

            direction = direction_temp
            temp = {self.ui.label_4.text(): {}}
            for l in self.ui.labels:
                    temp[self.ui.label_4.text()][l.text()] = {}
            for k,key in enumerate(temp[self.ui.label_4.text()]):
                    for b in self.ui.buttons[k]:
                            try:
                                    temp[self.ui.label_4.text()][key][b.text().split(" : ")[0]] = {"checkable":b.isEnabled(),"checked":False,"data_type":b.text().split(" : ")[1],
                                                                                                   "label":data["Domain"][domain_name][self.ui.label_4.text()][key][b.text().split(" : ")[0]]["label"],

                                                                                                   "type":data["Domain"][domain_name][self.ui.label_4.text()][key][b.text().split(" : ")[0]]["type"]}
                            except:
                                    temp[self.ui.label_4.text()][key][b.text().split(" : ")[0]] = {
                                            "checkable": b.isEnabled(), "checked": False,
                                            "data_type": b.text().split(" : ")[1]}
                            if b.isChecked()==True:
                                    temp[self.ui.label_4.text()][key][b.text().split(" : ")[0]]["checked"]=True
                            # print(data["Domain"][domain_name][self.ui.label_4.text()])
                            # print(data["Domain"][domain_name][self.ui.label_4.text()][key][b.text().split(" : ")[0]])

            #
            #print(len(self.ui.buttons),"===buttons")
            try:
                data_list[count]=temp
            except:
                data_list.append(temp)
            print(len(data_list))
            self.ui.labels = []
            self.ui.buttons=[]

            if count >= len(data["Domain"][domain_name])-1 and direction == True:
                    self.call_dbscreen()
            else:
                    if direction == True:
                        if back_exist==False:
                                next(self.screen_generator)
                        else:
                                self.ui.next_screen_normal()
                    elif count > 0:
                        back_exist=True
                        self.ui.back_screen()
                    else:
                        self.ui.stackedWidget.setCurrentWidget(self.ui.page_9)

            # #print(count)
    def call_back(self):
            global count
    def close(self):
        pass


# from sys import exit as sysExit
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # app.exec_()
    sys.exit(app.exec_())
