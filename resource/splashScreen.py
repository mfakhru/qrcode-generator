# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashScreen.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

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
        self.verticalLayout.setContentsMargins(50, 20, 50, 50)
        self.verticalSpacer = QSpacerItem(20, 155, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(Form)
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
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMinimumSize(QSize(0, 10))
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(7)
        font1.setBold(False)
        self.progressBar.setFont(font1)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"     border: 2px #E2E1E1;\n"
"     background-color: #E2E1E1;\n"
"	 text-align: right;\n"
"	 color: white;\n"
"	 border-radius: 4px;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"    background-color: rgb(84,144,249);\n"
"    width: 20px;\n"
" }")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(1)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.horizontalSpacer_6 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.mfakhru = QPushButton(Form)
        self.mfakhru.setObjectName(u"mfakhru")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        self.mfakhru.setFont(font2)
        self.mfakhru.setStyleSheet(u"background-color:white;\n"
"border: none;\n"
"color: black;")

        self.verticalLayout.addWidget(self.mfakhru)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"QR Code Generate", None))
        self.progressBar.setFormat(QCoreApplication.translate("Form", u"%p%", None))
        self.mfakhru.setText(QCoreApplication.translate("Form", u"created by mfakhru", None))
    # retranslateUi

