import sys, os
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Timelapse(QWidget):
    def __init__(self):
        super(Timelapse, self).__init__()
        self.t_start = 1.0
        self.t_stop = 1.5
        self.t_round = 1
        self.pos = 1 #1 = left, 2 = right
        self.callwin_timelapse()

    def callwin_timelapse(self):



        self.tpbg = QLabel(self)
        pixmap = QPixmap("img/blank_timelapse.png")
        self.tpbg.setPixmap(pixmap)

        self.minusBtn_start = QPushButton(self)
        self.minusBtn_start.setIcon(QIcon('img/btn_minus.png'))
        self.minusBtn_start.setIconSize(QSize(48,49))
        self.minusBtn_start.resize(48,49)
        self.minusBtn_start.move(34, 73)
        self.minusBtn_start.clicked.connect(self.startDown)

        self.plusBtn_start = QPushButton(self)
        self.plusBtn_start.setIcon(QIcon('img/btn_plus.png'))
        self.plusBtn_start.setIconSize(QSize(48,49))
        self.plusBtn_start.resize(48,49)
        self.plusBtn_start.move(183, 73)
        self.plusBtn_start.clicked.connect(self.startUp)

        self.minusBtn_stop = QPushButton(self)
        self.minusBtn_stop.setIcon(QIcon('img/btn_minus.png'))
        self.minusBtn_stop.setIconSize(QSize(48,49))
        self.minusBtn_stop.resize(48,49)
        self.minusBtn_stop.move(250, 73)
        self.minusBtn_stop.clicked.connect(self.stopDown)

        self.plusBtn_stop = QPushButton(self)
        self.plusBtn_stop.setIcon(QIcon('img/btn_plus.png'))
        self.plusBtn_stop.setIconSize(QSize(48,49))
        self.plusBtn_stop.resize(48,49)
        self.plusBtn_stop.move(399, 73)
        self.plusBtn_stop.clicked.connect(self.stopUp)

        self.plusBtn_round = QPushButton(self)
        self.plusBtn_round.setIcon(QIcon('img/btn_plus.png'))
        self.plusBtn_round.setIconSize(QSize(48,49))
        self.plusBtn_round.resize(48,49)
        self.plusBtn_round.move(183, 141)
        self.plusBtn_round.clicked.connect(self.roundUp)

        self.minusBtn_round = QPushButton(self)
        self.minusBtn_round.setIcon(QIcon('img/btn_minus.png'))
        self.minusBtn_round.setIconSize(QSize(48,49))
        self.minusBtn_round.resize(48,49)
        self.minusBtn_round.move(34, 141)
        self.minusBtn_round.clicked.connect(self.roundDown)





        self.selectBtn = QPushButton(self)
        self.swapPos()
        self.selectBtn.setIconSize(QSize(193,49))
        self.selectBtn.resize(193,49)
        self.selectBtn.move(252,143)
        self.selectBtn.clicked.connect(self.swapPos)

        self.timeStart = QLabel(self)
        show = QString("%1").arg(self.t_start)
        self.timeStart.setText(show)
        self.timeStart.setStyleSheet("QLabel{ color:#ffffff; font-size:25px; qproperty-alignment: AlignCenter;} ")
        self.timeStart.resize(90,39)
        self.timeStart.move(87, 81)

        self.timeStop = QLabel(self)
        show = QString("%1").arg(self.t_stop)
        self.timeStop.setText(show)
        self.timeStop.setStyleSheet("QLabel{ color:#ffffff; font-size:25px; qproperty-alignment: AlignCenter;} ")
        self.timeStop.resize(90,39)
        self.timeStop.move(304, 81)

        self.numRound = QLabel(self)
        show = QString("%1").arg(self.t_round)
        self.numRound.setText(show)
        self.numRound.setStyleSheet("QLabel{ color:#ffffff; font-size:25px; qproperty-alignment: AlignCenter;} ")
        self.numRound.resize(90,39)
        self.numRound.move(87, 149)

        self.statusTL = QLabel(self)
        self.statusTL.setText("connecting...")
        self.statusTL.setStyleSheet("QLabel{ color:#ffffff; font-size:20px; qproperty-alignment: AlignCenter;} ")
        self.statusTL.resize(374,40)
        self.statusTL.move(58, 198)

        self.startBtn_tl = QPushButton(self)
        self.startBtn_tl.setIcon(QIcon('img/btn_start_small.png'))
        self.startBtn_tl.setIconSize(QSize(104,56))
        self.startBtn_tl.resize(104,56)
        self.startBtn_tl.move(117,241)

        self.stopBtn_tl = QPushButton(self)
        self.stopBtn_tl.setIcon(QIcon('img/btn_stop_small.png'))
        self.stopBtn_tl.setIconSize(QSize(104,56))
        self.stopBtn_tl.resize(104,56)
        self.stopBtn_tl.move(256,241)

        self.setGeometry(0,0,480,320)
        self.setWindowTitle('Remote')
        self.show()

    def swapPos(self):

        if self.pos == 1:
            print 'pos = 1'
            self.selectBtn.setIcon(QIcon('img/btn_left.png'))
            self.pos = 2
        elif self.pos == 2:
            print 'pos = 2'
            self.selectBtn.setIcon(QIcon('img/btn_right.png'))
            self.pos = 1

    def startUp(self):
        self.t_start += 0.1
        show = QString("%1").arg(self.t_start)
        self.timeStart.setText(show)
    def startDown(self):
        if self.t_start > 0.2:
            self.t_start -= 0.1
        else:
            self.t_start = 0
        show = QString("%1").arg(self.t_start)
        self.timeStart.setText(show)

    def stopUp(self):
        self.t_stop += 0.1
        show = QString("%1").arg(self.t_stop)
        self.timeStop.setText(show)
    def stopDown(self):
        if self.t_stop > 0.1:
            self.t_stop -= 0.1
        else:
            self.t_stop = 0
        show = QString("%1").arg(self.t_stop)
        self.timeStop.setText(show)

    def roundUp(self):
        self.t_round += 1
        show = QString("%1").arg(self.t_round)
        self.numRound.setText(show)
    def roundDown(self):
        if self.t_round > 2:
            self.t_round -= 1
        else:
            self.t_round = 1
        show = QString("%1").arg(self.t_round)
        self.numRound.setText(show)






def main():
    app = QApplication(sys.argv)
    ex = Timelapse()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
