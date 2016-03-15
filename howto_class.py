from PyQt4.QtGui import *

class HowtoWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.window = QWidget()
        self.howto1 = QLabel(self)
        howto1.setGeometry( 0,0,480,320 )
        pixmap = QPixmap("img/howto_1.png")
        howto1.setPixmap(pixmap)
        howto1.move(0,0)
