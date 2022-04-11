# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogFilename.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout)

class Ui_InputFilename(object):
    def setupUi(self, InputFilename):
        if not InputFilename.objectName():
            InputFilename.setObjectName(u"InputFilename")
        InputFilename.resize(301, 174)
        InputFilename.setStyleSheet(u"QFrame#frame{\n"
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
"}\n"
"\n"
"QPushButton#cancelBtn{\n"
"	background-color: white;\n"
"	border-radius: 6px;\n"
"	color: black;\n"
"	border: 1px solid rgb(137,135,187);\n"
"}\n"
"\n"
"QPushButton#cancelBtn:hover{\n"
"	color:white;\n"
"	border-radius: 6px;\n"
"	background-color: red;\n"
"	border: 1px solid red;\n"
"}")
        self.verticalLayout = QVBoxLayout(InputFilename)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(InputFilename)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(5)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 15)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(15)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.lineEditFilename = QLineEdit(self.frame)
        self.lineEditFilename.setObjectName(u"lineEditFilename")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditFilename.sizePolicy().hasHeightForWidth())
        self.lineEditFilename.setSizePolicy(sizePolicy1)
        self.lineEditFilename.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.lineEditFilename.setFont(font1)

        self.verticalLayout_2.addWidget(self.lineEditFilename)

        self.frameBtn = QFrame(self.frame)
        self.frameBtn.setObjectName(u"frameBtn")
        sizePolicy.setHeightForWidth(self.frameBtn.sizePolicy().hasHeightForWidth())
        self.frameBtn.setSizePolicy(sizePolicy)
        self.frameBtn.setFrameShape(QFrame.StyledPanel)
        self.frameBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameBtn)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.doneBtn = QPushButton(self.frameBtn)
        self.doneBtn.setObjectName(u"doneBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doneBtn.sizePolicy().hasHeightForWidth())
        self.doneBtn.setSizePolicy(sizePolicy2)
        self.doneBtn.setMinimumSize(QSize(100, 30))
        self.doneBtn.setFont(font1)

        self.horizontalLayout.addWidget(self.doneBtn)

        self.cancelBtn = QPushButton(self.frameBtn)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy2.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy2)
        self.cancelBtn.setMinimumSize(QSize(100, 30))
        self.cancelBtn.setFont(font1)

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout_2.addWidget(self.frameBtn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(InputFilename)

        QMetaObject.connectSlotsByName(InputFilename)
    # setupUi

    def retranslateUi(self, InputFilename):
        InputFilename.setWindowTitle(QCoreApplication.translate("InputFilename", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("InputFilename", u"Filename", None))
        self.doneBtn.setText(QCoreApplication.translate("InputFilename", u"Done", None))
        self.cancelBtn.setText(QCoreApplication.translate("InputFilename", u"Cancel", None))
    # retranslateUi

