import sys, os
sys.path.insert(0,'.')

from PySide6 import QtGui, QtWidgets
from mainMenu import MainMenu
from screen.splashScreen import SplashScreen
import ctypes
import time


if __name__ == "__main__":

    #---------- Icon -----------
    myappid=u'mycomp.myprod.subprod.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(":/icon/icon.svg"))
    app.setApplicationDisplayName("QR Codes Generate")
    
    #----------Splash screen----
    splash = SplashScreen()
    window = MainMenu()

    splash.show()
    # window.showMaximized()

    for i in range(1, 100):
        #progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.01:
            app.processEvents()
    
    window.show()
    app.exec()
    os._exit(1)