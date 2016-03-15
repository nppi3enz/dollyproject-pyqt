import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DollyProject(QWidget):

   def __init__(self):
        super(DollyProject, self).__init__()
        self.initUI()

    #    self.stacked_layout = QStackedLayout() #create layout window
    #    self.stacked_layout.addWidget(self.create_mainwindow_layout)
    #    self.stacked_layout.setCurrentIndex(1)

    #    self.central_widget = QWidget()
    #    self.central_widget.setLayout(self.stacked_Layout)
    #    self.setCentralWidget(self.central_widget)


   def initUI(self):

        palette = QPalette()
        palette.setColor(QPalette.Background,QColor(36, 36, 36))
        self.setPalette(palette)
        self.create_mainwindow_layout()
        #self.howto1()
        #self.initial_layout = QVBoxLayout()
        #self.initial_layout.addWidget(self.create_mainwindow_layout)

        #self.select_crop_widget = QWidget()
        #self.select_crop_widget.setLayout(self.initial_layout)
        #self.select_crop_widget.setLayout(self.initial_layout)


        self.setWindowTitle('DollyProject')
        self.show()

   def create_mainwindow_layout(self):
        self.main_window_layout = QWidget()
        self.lbl = QLabel(self)
        pixmap = QPixmap("img/logo_menu.png")
        self.lbl.setPixmap(pixmap)
        self.lbl.move(140, 30)
        #self.main_window_layout.addWidget(self.lbl)


        btn1 = QPushButton("", self)
        btn1.setIcon(QIcon('img/mode_1.png'))
        btn1.setIconSize(QSize(138,145))
        btn1.resize(138,145)
        btn1.move(20, 90)
        self.connect(btn1,SIGNAL("clicked()"), self.howto1)

        btn2 = QPushButton("", self)
        btn2.setIcon(QIcon('img/mode_2.png'))
        btn2.setIconSize(QSize(138,145))
        btn2.resize(138,145)
        btn2.move(170, 90)

        btn3 = QPushButton("", self)
        btn3.setIcon(QIcon('img/mode_3.png'))
        btn3.setIconSize(QSize(138,145))
        btn3.resize(138,145)
        btn3.move(320, 90)

        about = QPushButton("", self)
        about.setIcon(QIcon('img/info.png'))
        about.setIconSize(QSize(53,53))
        about.resize(53,53)
        about.move(10, 260)
        about.clicked.connect(self.buttonClicked)

        close = QPushButton("", self)
        close.setIcon(QIcon('img/power.png'))
        close.setIconSize(QSize(53,53))
        close.resize(53,53)
        close.move(420, 260)
        close.clicked.connect(QCoreApplication.instance().quit)

        self.setGeometry(0, 0, 480, 320)

   def buttonClicked(self):
         msgBox = QMessageBox()
         msgBox.setText("Created by\nNipitpon Chantada\n5533684623")
         msgBox.setIcon(QMessageBox.Information)
         retval = msgBox.exec_()
         print "value of pressed message box button:", retval

   def howto1(self):
       print "howto1 screen"
       self.howto = QLabel(self)
       self.howto.setGeometry( 0,0,480,320 )
       pixmap = QPixmap("img/howto_1.png")
       self.howto.setPixmap(pixmap)
       self.howto.move(0,0)


def main():

    app = QApplication(sys.argv)
    ex = DollyProject()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
