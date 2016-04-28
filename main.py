import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from remote_class import *
from timelapse_class import *

class DollyProject(QWidget):


    def __init__(self, stack):
        #super(DollyProject, self).__init__()
        QWidget.__init__(self, stack)
        self.stack = stack
        self.initUI()
        self.mode_current = 0

    def initUI(self):

        #set background
        palette = QPalette()
        palette.setColor(QPalette.Background,QColor(36, 36, 36))
        self.setPalette(palette)

        self.stack1 = QWidget()
        self.mainwindow()
        #self.howto1()

        self.setGeometry(0,0,480,320)
        self.setWindowTitle('DollyProject')
        #self.showFullScreen()
        self.show()

    def mainwindow(self):
        print ('call mainwindow')
        self.lbl = QLabel(self)
        pixmap = QPixmap("img/logo_menu.png")
        self.lbl.setPixmap(pixmap)
        self.lbl.move(140, 30)

        self.btn1 = QPushButton(self)
        self.btn1.setIcon(QIcon('img/mode_1.png'))
        self.btn1.setIconSize(QSize(138,145))
        self.btn1.resize(138,145)
        self.btn1.move(20, 90)
        self.btn1.clicked.connect(self.howto1)

        self.btn2 = QPushButton(self)
        self.btn2.setIcon(QIcon('img/mode_2.png'))
        self.btn2.setIconSize(QSize(138,145))
        self.btn2.resize(138,145)
        self.btn2.move(170, 90)

        self.btn3 = QPushButton(self)
        self.btn3.setIcon(QIcon('img/mode_3.png'))
        self.btn3.setIconSize(QSize(138,145))
        self.btn3.resize(138,145)
        self.btn3.move(320, 90)
        self.btn3.clicked.connect(self.howto3)

        self.aboutBtn = QPushButton(self)
        self.aboutBtn.setIcon(QIcon('img/info.png'))
        self.aboutBtn.setIconSize(QSize(53,53))
        self.aboutBtn.resize(53,53)
        self.aboutBtn.move(10, 260)
        self.aboutBtn.clicked.connect(self.aboutme)

        self.close = QPushButton(self)
        self.close.setIcon(QIcon('img/power.png'))
        self.close.setIconSize(QSize(53,53))
        self.close.resize(53,53)
        self.close.move(420, 260)
        self.close.clicked.connect(QCoreApplication.instance().quit)

        #HIDE ITEM ALL-------------------------------------------
        self.lbl2 = QLabel(self)
        pixmap2 = QPixmap("img/howto_1.png")
        self.lbl2.setPixmap(pixmap2)
        self.lbl2.move(-1000, -1000)

        self.lbm3 = QLabel(self)
        pixmap = QPixmap("img/howto_3.png")
        self.lbm3.setPixmap(pixmap)
        self.lbm3.move(-1000, -1000)

        self.nextBtn = QPushButton('', self)
        self.nextBtn.setIcon(QIcon('img/nextBtn.png'))
        self.nextBtn.setIconSize(QSize(127,66))
        self.nextBtn.resize(127,66)
        self.nextBtn.move(-1000,-1000)
        self.nextBtn.clicked.connect(self.nextstep)


        self.homeBtn = QPushButton('', self)
        self.homeBtn.setIcon(QIcon('img/home_btn.png'))
        self.homeBtn.setIconSize(QSize(50,46))
        self.homeBtn.resize(50,46)
        self.homeBtn.move(-1000,-1000)
        self.homeBtn.clicked.connect(self.backhome)

        self.bgwin = QLabel(self)


    def howto1(self):
        print ('call howto1')
        self.mode_current = 1
        self.deleteObject()
        self.lbl2.move(0, 0)
        self.nextBtn.move(177, 237)
        self.homeBtn.move(5, 271)
        #self.aboutBtn.clicked.connect(self.backhome)
    def howto3(self):
        print ('call howto3')
        self.mode_current = 3
        self.deleteObject()
        self.lbm3.move(0, 0)
        self.nextBtn.move(177, 237)
        self.homeBtn.move(5, 271)

        #self.aboutBtn.clicked.connect(self.backhome)
    def nextstep(self):
        if self.mode_current == 1:
            #hide howto
            self.lbl2.move(-1000, -1000)
            self.nextBtn.move(-1000, -1000)
            self.remote()
        elif self.mode_current == 3:
            self.lbm3.move(-1000, -1000)
            self.nextBtn.move(-1000, -1000)
            self.timelapse()


    def backhome(self):
        print ('mode = ',self.mode_current)
        if self.mode_current == 1:
            self.lbl2.move(-1000, -1000)
        elif self.mode_current == 3:
            self.lbm3.move(-1000, -1000)
        self.nextBtn.move(-1000,-1000)
        self.homeBtn.move(-1000,-1000)
        self.refreshMain()


    def remote(self):
        print ('Mode remote is work')
        self.stack.setPage2()

    def timelapse(self):
        print ('Time Lapse is work')
        #self.lbm3.move(-1000, -1000)
        #self.nextBtn.move(-1000, -1000)

        self.stack.setPage3()

        #init_time(self, 1)
        #callwin_timelapse(self)
        #minusBtn_start.clicked.connect(self.startDown)

    def aboutme(self):
        msgBox = QMessageBox()
        msgBox.setText("Created by\nNipitpon Chantada\n5533684623")
        msgBox.setIcon(QMessageBox.Information)
        retval = msgBox.exec_()

    def deleteObject(self):
        print ("delete")
        #hide all
        self.lbl.move(-1000,-1000)
        self.btn1.move(-1000,-1000)
        self.btn2.move(-1000,-1000)
        self.btn3.move(-1000,-1000)
        self.aboutBtn.move(-1000,-1000)
        self.close.move(-1000,-1000)

    def refreshMain(self):
        self.lbl.move(140, 30)
        self.btn1.move(20, 90)
        self.btn2.move(170, 90)
        self.btn3.move(320, 90)
        self.aboutBtn.move(10, 260)
        self.close.move(420, 260)

    def goIndex(self):
        self.stack.setPage1()

class StackedWidget(QStackedWidget):

    def __init__(self, parent = None):
        QStackedWidget.__init__(self, parent)

    def setCurrentIndex(self, index):
        self.fader_widget = DollyProject(self.currentWidget())
        QStackedWidget.setCurrentIndex(self, index)

    def setPage1(self): #page index
        self.setCurrentIndex(0)

    def setPage2(self): #page remote

        self.setCurrentIndex(1)

    def setPage3(self): #page face-detection
        self.setCurrentIndex(2)

    def setPage4(self): #page timelapse
        self.setCurrentIndex(3)

def main():
    app = QApplication(sys.argv)
    #set foreground color
    palette = QPalette()
    palette.setColor(QPalette.Background,QColor(36, 36, 36))

    window = QWidget()
    window.setPalette(palette)
    #ex = DollyProject()
    stack = StackedWidget()
    stack.addWidget(DollyProject(stack))
    stack.addWidget(Remote(stack))
    stack.addWidget(Timelapse(stack))

    layout = QHBoxLayout(window)
    layout.addWidget(stack)
    window.move(0,0)
    window.resize(480,320)
    window.layout().setContentsMargins(0, 0, 0, 0)
    #window.show()
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
