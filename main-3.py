import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#from howto_class import *

class DollyProject(QWidget):

   def __init__(self):
        super(DollyProject, self).__init__()
        self.initUI()

        #create layout window
    #    self.stacked_layout.addWidget(self.HowtoWidget)
    #    self.stacked_layout.setCurrentIndex(1)

    #    self.central_widget = QWidget()
    #    self.central_widget.setLayout(self.stacked_Layout)
    #    self.setCentralWidget(self.central_widget)


   def initUI(self):

        palette = QPalette()
        palette.setColor(QPalette.Background,QColor(36, 36, 36))
        self.setPalette(palette)

        #self.create_mainwindow_layout()
        self.main_win = QWidget()
        self.stack1 = QWidget()

        self.mainwindow()
        self.stack1UI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.main_win)
        #self.Stack.addWidget(self.stack1)


        hbox = QVBoxLayout(self)
        hbox.addWidget(self.Stack)
        hbox.setGeometry(QRect(0,0,480,320))


        #self.setLayout(main_win)

        #self.lohowto1 = QWidget()
        #self.lohowto1.setLayout(self.howto1)

        #self.stacked_layout.addWidget(self.lohowto1)
        #self.create_mainwindow_layout()
        #self.howto1()
        #self.initial_layout = QVBoxLayout()
        #self.initial_layout.addWidget(self.create_mainwindow_layout)

        #self.select_crop_widget = QWidget()
        #self.select_crop_widget.setLayout(self.initial_layout)
        #self.select_crop_widget.setLayout(self.initial_layout)
        self.setGeometry(0,0,480,320)
        self.setWindowTitle('DollyProject')
        self.show()

   def stack1UI(self):
        layout = QHBoxLayout()
        #layout.addWidget(QLabel("subject"))
        howto1 = QLabel(self)
        howto1.setGeometry( 0,0,480,320 )
        pixmap = QPixmap("img/howto_1.png")
        howto1.setPixmap(pixmap)
        howto1.move(0,0)
        layout.addWidget(howto1)
        self.stack1.setLayout(layout)

   def display(self, i):
       self.Stack.setCurrentIndex(i)

   def mainwindow(self):
        layout = QWidget()
        lbl = QLabel(layout)
        pixmap = QPixmap("img/logo_menu.png")
        lbl.setPixmap(pixmap)
        lbl.move(140, 30)

        btn1 = QPushButton("", layout)
        btn1.setIcon(QIcon('img/mode_1.png'))
        btn1.setIconSize(QSize(138,145))
        btn1.resize(138,145)
        btn1.move(20, 90)
        #self.connect(btn1,SIGNAL("clicked()"), self.howto1)

        btn2 = QPushButton("", layout)
        btn2.setIcon(QIcon('img/mode_2.png'))
        btn2.setIconSize(QSize(138,145))
        btn2.resize(138,145)
        btn2.move(170, 90)

        btn3 = QPushButton("", layout)
        btn3.setIcon(QIcon('img/mode_3.png'))
        btn3.setIconSize(QSize(138,145))
        btn3.resize(138,145)
        btn3.move(320, 90)

        about = QPushButton("", layout)
        about.setIcon(QIcon('img/info.png'))
        about.setIconSize(QSize(53,53))
        about.resize(53,53)
        about.move(10, 260)
        #about.clicked.connect(self.buttonClicked)

        close = QPushButton("", layout)
        close.setIcon(QIcon('img/power.png'))
        close.setIconSize(QSize(53,53))
        close.resize(53,53)
        close.move(420, 260)
        #close.clicked.connect(QCoreApplication.instance().quit)

        #layout.resize(0, 0, 480, 320)
        #self.main_win.setLayout(layout)
        self.main_win = layout

   def buttonClicked(self):
         msgBox = QMessageBox()
         msgBox.setText("Created by\nNipitpon Chantada\n5533684623")
         msgBox.setIcon(QMessageBox.Information)
         retval = msgBox.exec_()
         print "value of pressed message box button:", retval

  # def howto1(self):
    #   print "howto1 screen"
     #  howto1 = QWidget()
      # howto1 = QLabel(self)
       #howto1.setGeometry( 0,0,480,320 )
       #pixmap = QPixmap("img/howto_1.png")
      # howto1.setPixmap(pixmap)
      # howto1.move(0,0)

       #self.stacked_layout.setCurrentIndex(0)


def main():

    app = QApplication(sys.argv)
    ex = DollyProject()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
