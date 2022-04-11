from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from resource.dialogInfo import Ui_Information


class DialogInfo(QDialog, Ui_Information):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.doneBtn.pressed.connect(self.accept)

   

   


if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = DialogInfo()
    window.show()
    app.exec()
    os._exit(1)
    