# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutApp.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 480)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255,255,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.homeBtn = QPushButton(self.frame_4)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(True)
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"background-color:white;\n"
"border: none;\n"
"color: black;")

        self.horizontalLayout_3.addWidget(self.homeBtn)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 0, 30, 30)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame)
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
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.mfakhru = QPushButton(self.frame)
        self.mfakhru.setObjectName(u"mfakhru")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        self.mfakhru.setFont(font3)
        self.mfakhru.setStyleSheet(u"background-color:white;\n"
"border: none;\n"
"color: black;")

        self.verticalLayout_2.addWidget(self.mfakhru)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.homeBtn.setText(QCoreApplication.translate("Form", u"Home >", None))
        self.label.setText(QCoreApplication.translate("Form", u"About", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Simple Desktop App for create your QR Codes with your favorite picture on the Desktop.", None))
        self.mfakhru.setText(QCoreApplication.translate("Form", u"created by mfakhru", None))
    # retranslateUi

