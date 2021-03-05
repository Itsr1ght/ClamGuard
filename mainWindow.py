# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowHAatTQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QSize(800, 600))
        mainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.dropshadowFrame = QFrame(self.centralwidget)
        self.dropshadowFrame.setObjectName(u"dropshadowFrame")
        self.dropshadowFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(55, 56, 59, 255));\n"
"border-radius: 5px;")
        self.dropshadowFrame.setFrameShape(QFrame.NoFrame)
        self.dropshadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.dropshadowFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.dropshadowFrame)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 30))
        self.titleBar.setStyleSheet(u"background-color:none;")
        self.titleBar.setFrameShape(QFrame.NoFrame)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleFrame = QFrame(self.titleBar)
        self.titleFrame.setObjectName(u"titleFrame")
        font = QFont()
        font.setFamily(u"SF Pro Display")
        self.titleFrame.setFont(font)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.title_label = QLabel(self.titleFrame)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setFamily(u"SF Pro Display")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"color: rgb(0, 255, 38);")

        self.horizontalLayout_2.addWidget(self.title_label)


        self.horizontalLayout.addWidget(self.titleFrame)

        self.titleButtons = QFrame(self.titleBar)
        self.titleButtons.setObjectName(u"titleButtons")
        self.titleButtons.setMaximumSize(QSize(70, 16777215))
        self.titleButtons.setFrameShape(QFrame.StyledPanel)
        self.titleButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.titleButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.minButton = QPushButton(self.titleButtons)
        self.minButton.setObjectName(u"minButton")
        self.minButton.setMinimumSize(QSize(16, 16))
        self.minButton.setMaximumSize(QSize(16, 16))
        self.minButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(176, 109, 16);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: rgb(255, 128, 0);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.minButton)

        self.closeButton = QPushButton(self.titleButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(16, 16))
        self.closeButton.setMaximumSize(QSize(16, 16))
        self.closeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: rgb(161, 0, 2);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: rgb(255, 0, 4);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.titleButtons)


        self.verticalLayout.addWidget(self.titleBar)

        self.mainInterface = QFrame(self.dropshadowFrame)
        self.mainInterface.setObjectName(u"mainInterface")
        font2 = QFont()
        font2.setFamily(u"SF Pro Text")
        self.mainInterface.setFont(font2)
        self.mainInterface.setStyleSheet(u"background-color:none;")
        self.mainInterface.setFrameShape(QFrame.NoFrame)
        self.mainInterface.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainInterface)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedHome = QStackedWidget(self.mainInterface)
        self.stackedHome.setObjectName(u"stackedHome")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.verticalLayout_4 = QVBoxLayout(self.pageHome)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.pageHome)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_content_home)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scanFrame = QFrame(self.frame_content_home)
        self.scanFrame.setObjectName(u"scanFrame")
        self.scanFrame.setMinimumSize(QSize(160, 160))
        self.scanFrame.setMaximumSize(QSize(160, 160))
        self.scanFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.scanFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: 5px solid rgb(0, 182, 24);\n"
"	border-radius: 80px;\n"
"}\n"
"QFrame:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")
        self.scanFrame.setFrameShape(QFrame.StyledPanel)
        self.scanFrame.setFrameShadow(QFrame.Raised)
        self.scanlabel = QLabel(self.scanFrame)
        self.scanlabel.setObjectName(u"scanlabel")
        self.scanlabel.setGeometry(QRect(50, 70, 61, 21))
        font3 = QFont()
        font3.setFamily(u"SF Pro Text")
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(75)
        self.scanlabel.setFont(font3)
        self.scanlabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(0, 255, 38);\n"
"	border:none;\n"
"}\n"
"\n"
"	")
        self.scanlabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.scanFrame)


        self.verticalLayout_4.addWidget(self.frame_content_home)

        self.stackedHome.addWidget(self.pageHome)
        self.pageScan = QWidget()
        self.pageScan.setObjectName(u"pageScan")
        self.verticalLayout_5 = QVBoxLayout(self.pageScan)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frameScan = QFrame(self.pageScan)
        self.frameScan.setObjectName(u"frameScan")
        self.frameScan.setFrameShape(QFrame.StyledPanel)
        self.frameScan.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frameScan)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.backButton = QPushButton(self.frameScan)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMinimumSize(QSize(120, 120))
        self.backButton.setMaximumSize(QSize(120, 120))
        font4 = QFont()
        font4.setFamily(u"SF Pro Display")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.backButton.setFont(font4)
        self.backButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.backButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 5px solid rgb(0, 182, 24);\n"
"	border-radius: 60px;\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.backButton)

        self.quickscanButton = QPushButton(self.frameScan)
        self.quickscanButton.setObjectName(u"quickscanButton")
        self.quickscanButton.setMinimumSize(QSize(120, 120))
        self.quickscanButton.setMaximumSize(QSize(120, 120))
        self.quickscanButton.setFont(font4)
        self.quickscanButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.quickscanButton.setAutoFillBackground(False)
        self.quickscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 5px solid rgb(0, 182, 24);\n"
"	border-radius: 60px;\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.quickscanButton)

        self.fullscanButton = QPushButton(self.frameScan)
        self.fullscanButton.setObjectName(u"fullscanButton")
        self.fullscanButton.setMinimumSize(QSize(120, 120))
        self.fullscanButton.setMaximumSize(QSize(120, 120))
        self.fullscanButton.setFont(font4)
        self.fullscanButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 5px solid rgb(0, 182, 24);\n"
"	border-radius: 60px;\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.fullscanButton)

        self.customscanButton = QPushButton(self.frameScan)
        self.customscanButton.setObjectName(u"customscanButton")
        self.customscanButton.setMinimumSize(QSize(120, 120))
        self.customscanButton.setMaximumSize(QSize(120, 120))
        self.customscanButton.setFont(font4)
        self.customscanButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.customscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 5px solid rgb(0, 182, 24);\n"
"	border-radius: 60px;\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.customscanButton)

        self.cancelscanButton = QPushButton(self.frameScan)
        self.cancelscanButton.setObjectName(u"cancelscanButton")
        self.cancelscanButton.setMinimumSize(QSize(120, 120))
        self.cancelscanButton.setMaximumSize(QSize(120, 120))
        self.cancelscanButton.setFont(font4)
        self.cancelscanButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 5px solid rgb(0, 182, 24);\n"
"	border-radius: 60px;\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(255,0,4);\n"
"	color: rgb(255,0,4);\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.cancelscanButton)


        self.verticalLayout_5.addWidget(self.frameScan)

        self.scanStatus = QPlainTextEdit(self.pageScan)
        self.scanStatus.setObjectName(u"scanStatus")
        self.scanStatus.setMinimumSize(QSize(765, 300))
        self.scanStatus.setMaximumSize(QSize(765, 300))
        self.scanStatus.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"	 \n"
"	background-color: rgb(33, 33, 33);\n"
"	color: rgb(0,255,38);\n"
"}\n"
"	")

        self.verticalLayout_5.addWidget(self.scanStatus)

        self.stackedHome.addWidget(self.pageScan)

        self.verticalLayout_3.addWidget(self.stackedHome)


        self.verticalLayout.addWidget(self.mainInterface)

        self.statusBar = QFrame(self.dropshadowFrame)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMaximumSize(QSize(16777215, 30))
        self.statusBar.setStyleSheet(u"background-color:none;")
        self.statusBar.setFrameShape(QFrame.NoFrame)
        self.statusBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.statusBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.databaseVer = QLabel(self.statusBar)
        self.databaseVer.setObjectName(u"databaseVer")
        font5 = QFont()
        font5.setFamily(u"SF Pro Display")
        font5.setPointSize(8)
        font5.setBold(True)
        font5.setWeight(75)
        self.databaseVer.setFont(font5)
        self.databaseVer.setStyleSheet(u"color: rgb(0, 255, 38);")

        self.verticalLayout_2.addWidget(self.databaseVer)


        self.verticalLayout.addWidget(self.statusBar)


        self.drop_shadow_layout.addWidget(self.dropshadowFrame)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.stackedHome.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ClamGuard", None))
        self.title_label.setText(QCoreApplication.translate("mainWindow", u"ClamGuard", None))
        self.minButton.setText("")
        self.closeButton.setText("")
        self.scanlabel.setText(QCoreApplication.translate("mainWindow", u"SCAN", None))
        self.backButton.setText(QCoreApplication.translate("mainWindow", u"Home", None))
        self.quickscanButton.setText(QCoreApplication.translate("mainWindow", u"Quick Scan", None))
        self.fullscanButton.setText(QCoreApplication.translate("mainWindow", u"Full Scan", None))
        self.customscanButton.setText(QCoreApplication.translate("mainWindow", u"Custom Scan", None))
        self.cancelscanButton.setText(QCoreApplication.translate("mainWindow", u"Cancel Scan", None))
        self.databaseVer.setText(QCoreApplication.translate("mainWindow", u"Database Version: ", None))
    # retranslateUi

