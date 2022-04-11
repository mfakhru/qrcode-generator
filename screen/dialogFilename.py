from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from resource.dialogFilename import Ui_InputFilename


class DialogInputFilename(QDialog, Ui_InputFilename):
    finnishGetFilename = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.lineEditFilename.setText("")

        self.doneBtn.clicked.connect(self.getFilename)
        self.cancelBtn.clicked.connect(self.reject)

    def getFilename(self):
        fileName = self.lineEditFilename.text()
        self.accept()
        self.finnishGetFilename.emit(fileName)

   


if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = DialogInputFilename()
    window.show()
    app.exec()
    os._exit(1)
    