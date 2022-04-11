# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(720, 480)
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 6px;\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"	border: 1px solid rgb(137,135,187);\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(84,144,249);\n"
"	border-radius: 6px;\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(20,146,230);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(84,144,249);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 50, 50, 50)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, -1, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.startedBtn = QPushButton(self.frame)
        self.startedBtn.setObjectName(u"startedBtn")
        sizePolicy1.setHeightForWidth(self.startedBtn.sizePolicy().hasHeightForWidth())
        self.startedBtn.setSizePolicy(sizePolicy1)
        self.startedBtn.setMinimumSize(QSize(150, 30))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.startedBtn.setFont(font1)

        self.verticalLayout_2.addWidget(self.startedBtn)

        self.aboutBtn = QPushButton(self.frame)
        self.aboutBtn.setObjectName(u"aboutBtn")
        sizePolicy1.setHeightForWidth(self.aboutBtn.sizePolicy().hasHeightForWidth())
        self.aboutBtn.setSizePolicy(sizePolicy1)
        self.aboutBtn.setMinimumSize(QSize(150, 30))
        self.aboutBtn.setFont(font1)

        self.verticalLayout_2.addWidget(self.aboutBtn)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mfakhru = QPushButton(self.frame_4)
        self.mfakhru.setObjectName(u"mfakhru")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        self.mfakhru.setFont(font2)
        self.mfakhru.setStyleSheet(u"background-color:white;\n"
"border: none;\n"
"color: black;")

        self.horizontalLayout_3.addWidget(self.mfakhru)


        self.verticalLayout.addWidget(self.frame_4)

        MainMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainMenu", u"QR Code Generate", None))
        self.startedBtn.setText(QCoreApplication.translate("MainMenu", u"Get started!", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainMenu", u"About", None))
        self.mfakhru.setText(QCoreApplication.translate("MainMenu", u"created by mfakhru", None))
    # retranslateUi

