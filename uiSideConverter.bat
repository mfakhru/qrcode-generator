:: QR Code Generator
:: author: mfakhru.github.io


:: main page
pyside6-uic -o resource/qrGenerate.py ui/qrGenerate.ui
pyside6-uic -o resource/mainMenu.py ui/mainMenu.ui
pyside6-uic -o resource/aboutApp.py ui/aboutApp.ui


:: splash screen
pyside6-uic -o resource/splashScreen.py ui/splashScreen.ui

:: dialog
pyside6-uic -o resource/dialogFilename.py ui/dialogFilename.ui
pyside6-uic -o resource/dialogInfo.py ui/dialogInfo.ui

:: icon
pyside6-rcc icon/icon.qrc -o icon_rc.py

pause