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

count = 0
domain_name = "hospitalManagement"
direction = None
data_list = []
back_exist=False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 863)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
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
        self.frame_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.454545, x2:1, y2:0.454545, stop:0 rgba(0, 30, 235, 255), stop:1 rgba(98, 0, 204, 255));")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_56 = QtWidgets.QFrame(self.frame)
        self.frame_56.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_56.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(".Aqua Kana")
        self.frame_56.setFont(font)
        self.frame_56.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 16, 140, 255), stop:1 rgba(32, 0, 221, 255));")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_56)
        self.horizontalLayout_35.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_22 = QtWidgets.QLabel(self.frame_56)
        font = QtGui.QFont()
        font.setFamily(".Lucida Grande UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:transparent;")
        self.label_22.setObjectName("label_22")
        # self.label_22.setText("yes")
        self.horizontalLayout_35.addWidget(self.label_22)
        self.frame_57 = QtWidgets.QFrame(self.frame_56)
        self.frame_57.setStyleSheet("background:transparent;")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.horizontalLayout_35.addWidget(self.frame_57)
        self.verticalLayout_24.addWidget(self.frame_56)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setSizeIncrement(QtCore.QSize(0, 500))
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
        self.horizontalLayout.setContentsMargins(-1, -1, 70, -1)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
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
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
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
        self.lineEdit.setMinimumSize(QtCore.QSize(186, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setStyleSheet("\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(30, 0, 217);\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"color: rgb(108, 108, 108);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(186, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_2.setStyleSheet("\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(30, 0, 217);\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"color: rgb(108, 108, 108);")
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
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 16, 140, 255), stop:1 rgba(32, 0, 221, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(self.page_2)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
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
"border-radius:10px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_8)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1030, 561))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout_6.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.page_2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_17 = QtWidgets.QFrame(self.frame_9)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 16, 140, 255), stop:1 rgba(32, 0, 221, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_11.addWidget(self.pushButton_2)
        self.horizontalLayout_9.addWidget(self.frame_17, 0, QtCore.Qt.AlignLeft)
        self.frame_18 = QtWidgets.QFrame(self.frame_9)
        self.frame_18.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_3.setMaximumSize(QtCore.QSize(41, 41))
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.5625, x2:1, y2:0.443, stop:0 rgba(57, 184, 3, 255), stop:1 rgba(59, 137, 5, 255));\n"
"border-radius:20px;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_12.addWidget(self.pushButton_3)
        self.horizontalLayout_9.addWidget(self.frame_18, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_9)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_20 = QtWidgets.QFrame(self.page_3)
        self.frame_20.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
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
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.verticalLayout_16.addWidget(self.frame_20)
        self.frame_22 = QtWidgets.QFrame(self.page_3)
        self.frame_22.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_16.addWidget(self.frame_22)
        self.frame_21 = QtWidgets.QFrame(self.page_3)
        self.frame_21.setMinimumSize(QtCore.QSize(200, 200))
        self.frame_21.setMaximumSize(QtCore.QSize(1621777, 1621777))
        self.frame_21.setStyleSheet("background-color: rgb(233, 233, 233);\n"
"border-radius:9px;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.frame_21)
        self.scrollArea_4.setMaximumSize(QtCore.QSize(250, 16777215))
        self.scrollArea_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 241, 320))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_25 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_25.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_25.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_10 = QtWidgets.QLabel(self.frame_25)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_15.addWidget(self.label_10, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_17.addWidget(self.frame_25)
        self.frame_23 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_23.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_17.addWidget(self.frame_23)
        self.frame_26 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_26.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_26.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.frame_26)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_17.addWidget(self.frame_26)
        self.frame_27 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_27.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_27.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_27.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_17.addWidget(self.frame_27)
        self.frame_28 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_28.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_11 = QtWidgets.QLabel(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_18.addWidget(self.label_11, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_17.addWidget(self.frame_28)
        self.frame_29 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_29.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_29.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_17.addWidget(self.frame_29)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_21.addWidget(self.scrollArea_4)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.frame_21)
        self.scrollArea_5.setMaximumSize(QtCore.QSize(250, 16777215))
        self.scrollArea_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 177, 314))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_30 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_30.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_13 = QtWidgets.QLabel(self.frame_30)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_20.addWidget(self.label_13, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_18.addWidget(self.frame_30)
        self.frame_24 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_24.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_24.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_18.addWidget(self.frame_24)
        self.frame_42 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_42.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_42.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_42)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_20 = QtWidgets.QLabel(self.frame_42)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_32.addWidget(self.label_20, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_18.addWidget(self.frame_42)
        self.frame_32 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_32.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_18.addWidget(self.frame_32)
        self.frame_33 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_33.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_33.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_33)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_15 = QtWidgets.QLabel(self.frame_33)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_23.addWidget(self.label_15, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_18.addWidget(self.frame_33)
        self.frame_34 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_34.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_34.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_18.addWidget(self.frame_34)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_21.addWidget(self.scrollArea_5)
        self.scrollArea_6 = QtWidgets.QScrollArea(self.frame_21)
        self.scrollArea_6.setMaximumSize(QtCore.QSize(250, 16777215))
        self.scrollArea_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 216, 314))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_36 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_36.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_36.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_36)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_16 = QtWidgets.QLabel(self.frame_36)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_26.addWidget(self.label_16, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_19.addWidget(self.frame_36)
        self.frame_35 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_35.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_35.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.verticalLayout_19.addWidget(self.frame_35)
        self.frame_37 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_37.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_37.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_37)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_17 = QtWidgets.QLabel(self.frame_37)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_27.addWidget(self.label_17, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_19.addWidget(self.frame_37)
        self.frame_38 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_38.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_38.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.verticalLayout_19.addWidget(self.frame_38)
        self.frame_39 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_39.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_39.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_18 = QtWidgets.QLabel(self.frame_39)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_29.addWidget(self.label_18, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_19.addWidget(self.frame_39)
        self.frame_40 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_40.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_40.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_40)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.verticalLayout_19.addWidget(self.frame_40)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_21.addWidget(self.scrollArea_6)
        self.verticalLayout_16.addWidget(self.frame_21)
        self.frame_19 = QtWidgets.QFrame(self.page_3)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_41 = QtWidgets.QFrame(self.frame_19)
        self.frame_41.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_41.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
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
        self.frame_31.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_31.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_43 = QtWidgets.QFrame(self.frame_31)
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_43)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_43)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 16, 140, 255), stop:1 rgba(32, 0, 221, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_14.addWidget(self.pushButton_4)
        self.horizontalLayout_10.addWidget(self.frame_43, 0, QtCore.Qt.AlignLeft)
        self.frame_44 = QtWidgets.QFrame(self.frame_31)
        self.frame_44.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_44)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_44)
        self.pushButton_5.setMaximumSize(QtCore.QSize(41, 41))
        self.pushButton_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.5625, x2:1, y2:0.443, stop:0 rgba(57, 184, 3, 255), stop:1 rgba(59, 137, 5, 255));\n"
"border-radius:20px;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_15.addWidget(self.pushButton_5)
        self.horizontalLayout_10.addWidget(self.frame_44, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_16.addWidget(self.frame_31)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_45 = QtWidgets.QFrame(self.page_4)
        self.frame_45.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_45.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_45.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.label_14 = QtWidgets.QLabel(self.frame_45)
        self.label_14.setGeometry(QtCore.QRect(12, 12, 242, 29))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setTextFormat(QtCore.Qt.PlainText)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_23.addWidget(self.frame_45)
        self.frame_46 = QtWidgets.QFrame(self.page_4)
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_46)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.frame_47 = QtWidgets.QFrame(self.frame_46)
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_47)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_47)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(186, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_3.setStyleSheet("\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(30, 0, 217);\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"color: rgb(108, 108, 108);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_20.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_47)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(186, 0))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_4.setStyleSheet("\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(30, 0, 217);\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"color: rgb(108, 108, 108);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_20.addWidget(self.lineEdit_4)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_47)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(186, 0))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_6.setStyleSheet("\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(30, 0, 217);\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"color: rgb(108, 108, 108);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_20.addWidget(self.lineEdit_6)
        self.horizontalLayout_34.addWidget(self.frame_47)
        self.frame_48 = QtWidgets.QFrame(self.frame_46)
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_48)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_48)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(186, 0))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_7.setStyleSheet("\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(30, 0, 217);\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"color: rgb(108, 108, 108);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_21.addWidget(self.lineEdit_7)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_48)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(186, 0))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_9.setStyleSheet("\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(30, 0, 217);\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"color: rgb(108, 108, 108);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_21.addWidget(self.lineEdit_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_48)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(186, 0))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(240, 16777215))
        self.lineEdit_8.setStyleSheet("\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(30, 0, 217);\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"color: rgb(108, 108, 108);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_21.addWidget(self.lineEdit_8)
        self.horizontalLayout_34.addWidget(self.frame_48)
        self.verticalLayout_23.addWidget(self.frame_46)
        self.frame_49 = QtWidgets.QFrame(self.page_4)
        self.frame_49.setMaximumSize(QtCore.QSize(200, 100))
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_49)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 20, 165, 50))
        self.pushButton_6.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_6.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("\n"
"background-color: rgb(253, 155, 53);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_23.addWidget(self.frame_49)
        self.frame_50 = QtWidgets.QFrame(self.page_4)
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.textEdit = QtWidgets.QTextEdit(self.frame_50)
        self.textEdit.setGeometry(QtCore.QRect(13, 13, 461, 61))
        self.textEdit.setMidLineWidth(200)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_50)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 90, 521, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_23.addWidget(self.frame_50)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.frame_51 = QtWidgets.QFrame(self.page_5)
        self.frame_51.setGeometry(QtCore.QRect(20, 100, 1011, 531))
        self.frame_51.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_51.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_51.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.label_21 = QtWidgets.QLabel(self.frame_51)
        self.label_21.setGeometry(QtCore.QRect(12, 12, 242, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setTextFormat(QtCore.Qt.PlainText)
        self.label_21.setObjectName("label_21")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_51)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 70, 391, 81))
        self.textEdit_3.setObjectName("textEdit_3")
        self.frame_52 = QtWidgets.QFrame(self.frame_51)
        self.frame_52.setGeometry(QtCore.QRect(30, 120, 351, 271))
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_52)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, 90, 104, 78))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.frame_53 = QtWidgets.QFrame(self.frame_51)
        self.frame_53.setGeometry(QtCore.QRect(10, 430, 1011, 98))
        self.frame_53.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_53.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_53)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_53)
        self.pushButton_7.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_7.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 16, 140, 255), stop:1 rgba(32, 0, 221, 255));\n"
"color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_33.addWidget(self.pushButton_7)
        self.frame_54 = QtWidgets.QFrame(self.frame_53)
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_54)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_33.addWidget(self.frame_54, 0, QtCore.Qt.AlignLeft)
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
        # self.create_cards()
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
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
            for t in data_list[count]:
                    key_value=t
                    break
            #print(data_list[count],"piaza2")
            self.label_4.setText(key_value)

            #print(data_list[count],"piaza")
            #print(key_value)
            return self.create_cards(data_list[count][key_value])
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
                    self.frame_10.setStyleSheet("background-color: rgb(233, 233, 233);\n"
                                                "border-radius:9px;")
                    self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.frame_10.setObjectName("frame_10")
                    self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
                    self.verticalLayout_7.setObjectName("verticalLayout_7")
                    self.frame_12 = QtWidgets.QFrame(self.frame_10)
                    self.frame_12.setMaximumSize(QtCore.QSize(600, 50))
                    # self.frame_12.setMinimumSize(QtCore.QSize(600, 60))
                    self.frame_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
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
                    self.label_5.setText(value)
                    self.labels.append(self.label_5)
                    # temp[self.label_4.text()][self.label_5.text()] = {}
                    # #print(value)

                    self.horizontalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
                    self.verticalLayout_7.addWidget(self.frame_12)
                    self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_10)
                    self.scrollArea_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                    "border-radius:10px;")
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
                            self.frame_13.setStyleSheet("background-color: rgb(235, 235, 235);\n"
                                                        "")
                            self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
                            self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
                            self.frame_13.setObjectName("frame_13")
                            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_13)
                            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                            self.checkBox = QtWidgets.QCheckBox(self.frame_13)
                            self.checkBox.setObjectName("checkBox")
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
                                    print(e)
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
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_22.setText(_translate("MainWindow", "Welcome Back"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.lineEdit.setText(_translate("MainWindow", " User Name"))
        self.lineEdit_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Forget password?"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        # self.label_4.setText(_translate("MainWindow", data["domain"]))
        try:
                self.label_5.setText(_translate("MainWindow", "Health Care Delivery Role"))
                self.checkBox.setText(_translate("MainWindow", "From Date"))
                self.checkBox_2.setText(_translate("MainWindow", "Thru Date"))
        except: pass
        self.pushButton_2.setText(_translate("MainWindow", "Back"))
        self.label_8.setText(_translate("MainWindow", "Prototype|Preferences"))
        self.label_9.setText(_translate("MainWindow", "Prototype Styling"))
        self.label_10.setText(_translate("MainWindow", "General Button Theme"))
        self.label_12.setText(_translate("MainWindow", "General Button color"))
        self.label_11.setText(_translate("MainWindow", "General Button Style"))
        self.label_13.setText(_translate("MainWindow", "Interface Color"))
        self.label_20.setText(_translate("MainWindow", "Interface Size"))
        self.label_15.setText(_translate("MainWindow", "Layout Style"))
        self.label_16.setText(_translate("MainWindow", "Alter Button Theme"))
        self.label_17.setText(_translate("MainWindow", "Color"))
        self.label_18.setText(_translate("MainWindow", "Style"))
        self.label_19.setText(_translate("MainWindow", "Output"))
        self.checkBox_4.setText(_translate("MainWindow", "Generate SQl Queries"))
        self.checkBox_5.setText(_translate("MainWindow", "Generate Prototype"))
        self.checkBox_6.setText(_translate("MainWindow", "Save DB File"))
        self.pushButton_4.setText(_translate("MainWindow", "Back"))
        self.label_14.setText(_translate("MainWindow", "Database Connection"))
        self.lineEdit_3.setText(_translate("MainWindow", "Database Name"))
        self.lineEdit_4.setText(_translate("MainWindow", "Port"))
        self.lineEdit_6.setText(_translate("MainWindow", "User Name"))
        self.lineEdit_7.setText(_translate("MainWindow", "Connection Name"))
        self.lineEdit_9.setText(_translate("MainWindow", "Host Name"))
        self.lineEdit_8.setText(_translate("MainWindow", "Password"))
        self.pushButton_6.setText(_translate("MainWindow", "Test Connection"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Notes</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Do not close the application until process finished.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.keep your internet conected if your database is remove</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "Please Wait..."))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stay connected with us while we are preparing your schema and prototype...</p></body></html>"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "image"))
        self.pushButton_7.setText(_translate("MainWindow", "Create New"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "IMAGE UML\n"
""))


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowTitle('')
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.movie = QMovie("83426-database.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.set_shadow()
        self.ui.frame_6.hide()
        self.button_connection()
        initializeDB()
        self.screen_generator=self.ui.create_screen()
        # self.back_screen_generator=self.ui.back_screen()
        self.ui.buttons=[]
        self.ui.labels=[]
    def call_dbscreen(self):
            #print("db screen")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
    def button_connection(self):
            self.ui.pushButton.clicked.connect(self.callAuth)

            self.ui.pushButton_3.clicked.connect(lambda:self.call_next(True))

            self.ui.pushButton_2.clicked.connect(lambda: self.call_next(False))
    def set_shadow(self):
        shadow = QGraphicsDropShadowEffect(xOffset=1, yOffset=1)
        shadow.setBlurRadius(80)

        # adding shadow to the label
        self.ui.frame_3.setGraphicsEffect(shadow)
    def callAuth(self):
        username = self.ui.lineEdit.text().casefold()
        password = self.ui.lineEdit_2.text()
        if auth(username,password) == True:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Username or Password is wrong')
                msg.setWindowTitle("Error")
                msg.exec_()
    def call_next(self, direction_temp):
            global count, domain_name, direction,data_list, back_exist
            direction = direction_temp
            temp = {self.ui.label_4.text(): {}}
            for l in self.ui.labels:
                    temp[self.ui.label_4.text()][l.text()] = {}
            for k,key in enumerate(temp[self.ui.label_4.text()]):
                    for b in self.ui.buttons[k]:
                            temp[self.ui.label_4.text()][key][b.text().split(" : ")[0]] = {"checkable":b.isEnabled(),"checked":False,"data_type":b.text().split(" : ")[1]}
                            if b.isChecked()==True:
                                    temp[self.ui.label_4.text()][key][b.text().split(" : ")[0]]["checked"]=True

            #
            #print(len(self.ui.buttons),"===buttons")
            try:
                data_list[count]=temp
            except:
                data_list.append(temp)
            print(len(data_list))
            self.ui.labels = []
            self.ui.buttons=[]

            if count == len(data["Domain"][domain_name]) and direction == True:
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
