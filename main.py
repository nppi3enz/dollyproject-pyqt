
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

   def __init__(self):
        super(Example, self).__init__()

        self.initUI()

   def initUI(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background,QtGui.QColor(36, 36, 36))
        self.setPalette(palette)

        self.lbl = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap("img/logo_menu.png")
        self.lbl.setPixmap(pixmap)
        self.lbl.move(140, 30)

        btn1 = QtGui.QPushButton("", self)
        btn1.setIcon(QtGui.QIcon('img/mode_1.png'))
        btn1.setIconSize(QtCore.QSize(138,145))
        btn1.resize(138,145)
        btn1.move(20, 90)

        btn2 = QtGui.QPushButton("", self)
        btn2.setIcon(QtGui.QIcon('img/mode_2.png'))
        btn2.setIconSize(QtCore.QSize(138,145))
        btn2.resize(138,145)
        btn2.move(170, 90)

        btn3 = QtGui.QPushButton("", self)
        btn3.setIcon(QtGui.QIcon('img/mode_3.png'))
        btn3.setIconSize(QtCore.QSize(138,145))
        btn3.resize(138,145)
        btn3.move(320, 90)

        about = QtGui.QPushButton("", self)
        about.setIcon(QtGui.QIcon('img/info.png'))
        about.setIconSize(QtCore.QSize(53,53))
        about.resize(53,53)
        about.move(10, 260)
        about.clicked.connect(self.buttonClicked)

        close = QtGui.QPushButton("", self)
        close.setIcon(QtGui.QIcon('img/power.png'))
        close.setIconSize(QtCore.QSize(53,53))
        close.resize(53,53)
        close.move(420, 260)
        close.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.setGeometry(0, 0, 480, 320)
        self.setWindowTitle('DollyProject')
        self.show()

   def buttonClicked(self):
         msgBox = QtGui.QMessageBox()
         msgBox.setText("Created by\nNipitpon Chantada\n5533684623")
         msgBox.setIcon(QtGui.QMessageBox.Information)
         retval = msgBox.exec_()
         print "value of pressed message box button:", retval

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
