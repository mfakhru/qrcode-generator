# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogInfo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout)
import icon_rc

class Ui_Information(object):
    def setupUi(self, Information):
        if not Information.objectName():
            Information.setObjectName(u"Information")
        Information.resize(304, 174)
        Information.setStyleSheet(u"QFrame#frame{\n"
"	background-color: rgb(255,255,255);\n"
"	border-radius: 8px;\n"
"	border: 2px solid rgb(137,135,187);\n"
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
"QPushButton#doneBtn{\n"
"	background-color: rgb(84,144,249);\n"
"	border-radius: 6px;\n"
"	color: rgb(255,255,255);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton#doneBtn:hover{\n"
"	color: rgb(20,146,230);\n"
"	background-color: rgb(255,255,255);\n"
"	border: 1px solid rgb(84,144,249);\n"
"}")
        self.verticalLayout = QVBoxLayout(Information)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Information)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(10)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 15)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.doneBtn_2 = QPushButton(self.frame_2)
        self.doneBtn_2.setObjectName(u"doneBtn_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doneBtn_2.sizePolicy().hasHeightForWidth())
        self.doneBtn_2.setSizePolicy(sizePolicy)
        self.doneBtn_2.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.doneBtn_2.setFont(font)
        self.doneBtn_2.setStyleSheet(u"background-color:none;\n"
"border:none;")
        icon = QIcon()
        icon.addFile(u":/icon/information.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.doneBtn_2.setIcon(icon)
        self.doneBtn_2.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.doneBtn_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frameBtn = QFrame(self.frame)
        self.frameBtn.setObjectName(u"frameBtn")
        sizePolicy1.setHeightForWidth(self.frameBtn.sizePolicy().hasHeightForWidth())
        self.frameBtn.setSizePolicy(sizePolicy1)
        self.frameBtn.setFrameShape(QFrame.StyledPanel)
        self.frameBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameBtn)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.doneBtn = QPushButton(self.frameBtn)
        self.doneBtn.setObjectName(u"doneBtn")
        sizePolicy.setHeightForWidth(self.doneBtn.sizePolicy().hasHeightForWidth())
        self.doneBtn.setSizePolicy(sizePolicy)
        self.doneBtn.setMinimumSize(QSize(100, 30))
        self.doneBtn.setFont(font)

        self.horizontalLayout.addWidget(self.doneBtn)


        self.verticalLayout_2.addWidget(self.frameBtn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Information)

        QMetaObject.connectSlotsByName(Information)
    # setupUi

    def retranslateUi(self, Information):
        Information.setWindowTitle(QCoreApplication.translate("Information", u"Dialog", None))
        self.doneBtn_2.setText("")
        self.label.setText(QCoreApplication.translate("Information", u"Please input your", None))
        self.label_2.setText(QCoreApplication.translate("Information", u"link address!", None))
        self.doneBtn.setText(QCoreApplication.translate("Information", u"OK", None))
    # retranslateUi

