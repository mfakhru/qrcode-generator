import os,sys
sys.path.insert(0,'.')

from screen.aboutScreen import AboutScreen
from screen.mainGenerate import MainGenerate

import webbrowser
from resource.mainMenu import Ui_MainMenu

from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MainMenu(QMainWindow, Ui_MainMenu):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Main Menu")

        self.mainGenerate = MainGenerate()
        self.aboutScreen = AboutScreen()

        self.startedBtn.clicked.connect(self.openMainGenerate)
        self.aboutBtn.clicked.connect(self.openAbout)

        self.mainGenerate.homeBtn.clicked.connect(lambda: self.backToHome("main"))
        self.aboutScreen.homeBtn.clicked.connect(lambda: self.backToHome("about"))

        self.mfakhru.clicked.connect(self.openCreated)

    def openMainGenerate(self):
        self.mainGenerate.show()
        self.setHidden(True)

    def openAbout(self):
        self.aboutScreen.show()
        self.setHidden(True)

    def backToHome(self, screen):
        if screen == "about":
            self.aboutScreen.close()
            self.setHidden(False)
            return
        self.mainGenerate.close()
        self.setHidden(False)


    def openCreated(self):
        webbrowser.open("https://mfakhru.github.io/")

if __name__ == "__main__":
    import os,sys

    def hello(filePath):
        print(f"Hello {filePath}")

    app = QApplication(sys.argv)

    
    window = MainMenu()
    window.show()
    sys.exit(app.exec())