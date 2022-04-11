import os,sys
sys.path.insert(0,'.')

import webbrowser
from resource.aboutApp import Ui_Form

from PySide6.QtWidgets import *
from PySide6.QtCore import *

class AboutScreen(QWidget, Ui_Form):


    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("About")

        self.mfakhru.clicked.connect(self.openCreated)

    def openCreated(self):
        webbrowser.open("https://mfakhru.github.io/")

if __name__ == "__main__":
    import os,sys

    def hello(filePath):
        print(f"Hello {filePath}")

    app = QApplication(sys.argv)

    
    window = AboutScreen()
    window.show()
    sys.exit(app.exec())