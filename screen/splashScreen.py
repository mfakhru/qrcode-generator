import sys, threading, time
sys.path.insert(0,'.')

from resource.splashScreen import Ui_Form

from PySide6.QtWidgets import *
from PySide6.QtCore import *

class SplashScreen(QWidget, Ui_Form):

    progSignal = Signal(int)
    finnisSignal = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # self.showMaximized()
        self.progSignal.connect(self.progressBar.setValue)
        tread = threading.Thread(target=self.progress,daemon=True)
        tread.start()

        self.finnisSignal.connect(self.close)
        

    def progress(self):
        for i in range(1, 100):
            #progressBar.setValue(i)
            self.progSignal.emit(i+1)
            time.sleep(0.01)
        self.finnisSignal.emit()


if __name__ == "__main__":
    import os,sys

    def hello(filePath):
        print(f"Hello {filePath}")

    app = QApplication(sys.argv)

    
    window = SplashScreen()
    
    sys.exit(app.exec())