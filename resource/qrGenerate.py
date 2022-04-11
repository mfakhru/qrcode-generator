# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qrGenerate.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icon_rc

class Ui_QRGenerate(object):
    def setupUi(self, QRGenerate):
        if not QRGenerate.objectName():
            QRGenerate.setObjectName(u"QRGenerate")
        QRGenerate.resize(720, 480)
        self.centralwidget = QWidget(QRGenerate)
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
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.homeBtn = QPushButton(self.frame_5)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(True)
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"background-color:white;\n"
"border: none;\n"
"color: black;")

        self.horizontalLayout_4.addWidget(self.homeBtn)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 0, 30, 30)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame_3 = QFrame(self.frame_6)
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
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(15)
        self.label_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEditAddress = QLineEdit(self.frame_2)
        self.lineEditAddress.setObjectName(u"lineEditAddress")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditAddress.sizePolicy().hasHeightForWidth())
        self.lineEditAddress.setSizePolicy(sizePolicy1)
        self.lineEditAddress.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        self.lineEditAddress.setFont(font3)

        self.verticalLayout_2.addWidget(self.lineEditAddress)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.openBtn = QPushButton(self.frame)
        self.openBtn.setObjectName(u"openBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.openBtn.sizePolicy().hasHeightForWidth())
        self.openBtn.setSizePolicy(sizePolicy2)
        self.openBtn.setMinimumSize(QSize(150, 30))
        self.openBtn.setFont(font3)

        self.horizontalLayout.addWidget(self.openBtn)

        self.doneBtn = QPushButton(self.frame)
        self.doneBtn.setObjectName(u"doneBtn")
        sizePolicy2.setHeightForWidth(self.doneBtn.sizePolicy().hasHeightForWidth())
        self.doneBtn.setSizePolicy(sizePolicy2)
        self.doneBtn.setMinimumSize(QSize(150, 30))
        self.doneBtn.setFont(font3)

        self.horizontalLayout.addWidget(self.doneBtn)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.mfakhru = QPushButton(self.frame_4)
        self.mfakhru.setObjectName(u"mfakhru")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        self.mfakhru.setFont(font4)
        self.mfakhru.setStyleSheet(u"background-color:white;\n"
"border: none;\n"
"color: black;")

        self.horizontalLayout_3.addWidget(self.mfakhru)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_6)

        QRGenerate.setCentralWidget(self.centralwidget)

        self.retranslateUi(QRGenerate)

        QMetaObject.connectSlotsByName(QRGenerate)
    # setupUi

    def retranslateUi(self, QRGenerate):
        QRGenerate.setWindowTitle(QCoreApplication.translate("QRGenerate", u"MainWindow", None))
        self.homeBtn.setText(QCoreApplication.translate("QRGenerate", u"Home >", None))
        self.label.setText(QCoreApplication.translate("QRGenerate", u"QR Code Generate", None))
        self.label_2.setText(QCoreApplication.translate("QRGenerate", u"Input Link Address", None))
        self.openBtn.setText(QCoreApplication.translate("QRGenerate", u"Add Image", None))
        self.doneBtn.setText(QCoreApplication.translate("QRGenerate", u"Save", None))
        self.mfakhru.setText(QCoreApplication.translate("QRGenerate", u"created by mfakhru", None))
    # retranslateUi

