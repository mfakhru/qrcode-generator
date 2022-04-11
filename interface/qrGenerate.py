import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class QRCodeGenerate(QThread):
    finishGenerate = Signal()

    def __init__(self) -> None:
        super().__init__()
        
    def setImage(self, path):
        if path == None:
            face = None
            return face
        face = Image.open(path)
        newSize = (90, 90)
        face = face.resize(newSize)
        return face

    def qrGenerate(self, address, path, fileName):
        print("Running..")

        face = self.setImage(path)
        qrBig = qrcode.QRCode(version=6,
            error_correction=qrcode.constants.ERROR_CORRECT_L)
        qrBig.add_data(address)
        qrBig.make()

        imageQrBig = qrBig.make_image(image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer()).convert('RGB')

        if face != None:
            pos = ((imageQrBig.size[0] - face.size[0])//2, (imageQrBig.size[1] - face.size[1])//2)
            imageQrBig.paste(face, pos)

        imageQrBig.save(f"C:/Users/admin/Pictures/{fileName}.png")
        print("Done")
        self.finishGenerate.emit()


if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = QRCodeGenerate()
    window.qrGenerate("mfakhru.github.io", "myimage.png", "my-qr-code" )
    window.start()
    app.exec()
    os._exit(1)
    