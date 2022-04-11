import webbrowser, sys
sys.path.insert(0,'.')

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from resource.qrGenerate import Ui_QRGenerate
from screen.dialogFilename import DialogInputFilename
from screen.dialogInfo import DialogInfo
from interface.qrGenerate import QRCodeGenerate


class MainGenerate(QMainWindow, Ui_QRGenerate):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("QR Code Generate")

        self.mfakhru.clicked.connect(self.openCreated)

        self.openBtn.clicked.connect(self.openImage)
        self.doneBtn.clicked.connect(self.startGen)
        self.filter = 'PNG (*.png);; JPEG (*.jpg *jpeg ".jpe" ".jp2");;BMP (*.bmp);;TIFF (*.tiff)'

        self.startGenerate = QRCodeGenerate()
        self.startGenerate.finishGenerate.connect(self.refreshContent)

        self.dialogInfo = DialogInfo()
        self.dialogFilename = DialogInputFilename()
        self.dialogFilename.finnishGetFilename.connect(self.refreshFilename)

        self.imagePath = None
        self.fileName = "default_name"

    def openCreated(self):
        webbrowser.open("https://mfakhru.github.io/")

    def refreshContent(self):
        self.imagePath = None
    
    def refreshFilename(self, fileName):
        print(fileName)
        self.fileName = fileName

    def openImage(self):
        imagePath = QFileDialog.getOpenFileName(self,"Open File",filter=self.filter)[0]
        self.imagePath = imagePath

    def startGen(self):
        address = self.lineEditAddress.text()
        if address == "":
            self.dialogInfo.exec()
            return
        state = self.dialogFilename.exec()
        if state != 1:
            return

        self.startGenerate.qrGenerate(address=address, path=self.imagePath, fileName=self.fileName)



if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = MainGenerate()
    window.show()
    app.exec()
    os._exit(1)
    