import sys, os
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import microgear.client as client
import time
class netpie(QThread):
    mySignal = pyqtSignal(object)

    def __init__(self):
        QThread.__init__(self)
        self.welcome()
        self.mySignal.emit('load')
        self.create_client()
        #self.start_connect()


    def create_client(self):
       gearkey = 'K0v7QsvD5AgzE0n'
       gearsecret =  'tGEE3SdcIpo2sDfzx3mHqKcm4Jd92s'
       appid = 'DollyProject'
       client.create(gearkey,gearsecret,appid)

    def start_connect(self):
        self.mySignal.emit('load')
        client.setname("remote")
        client.setalias("pyqt")
        client.on_connect = self.connection
        client.on_message = self.subscription
        client.on_disconnect = self.disconnect
        client.subscribe("/remote")
        client.connect()
        #while True:
    #        client.chat("doraemon","Hello world. "+str(int(time.time())))
    #        time.sleep(2)

    def connection(self):
        print ('Now I am connected with netpie console')
        self.mySignal.emit('STOP') #default at stop

    def disconnect(self):
        print ('Disconnected!!')

    def subscription(self,topic,message):
        #print topic+" "+message
        self.mySignal.emit(message)

    def welcome(self):
        print ('Welcome to NETPIE')

class Remote(QWidget):
    def __init__(self, net):
        super(Remote, self).__init__()
        self.net = net
        self.initUI()
        self.net.mySignal.connect(self.fetch_network)
        self.net.start_connect()

    def initUI(self):
        self.callwindow()
        self.fetch_network('load')

        self.setGeometry(0,0,480,320)
        self.setWindowTitle('Remote')
        self.show()

    def callwindow(self):
        self.lbl = QLabel(self)
        pixmap = QPixmap("img/blank_remote.png")
        self.lbl.setPixmap(pixmap)
        #self.lbl.setGeometry(0,0,480,320)
        #self.lbl.move(140, 30)
        self.status = QLabel(self)
        self.status.move(48,63)

        self.labelMotor = QLabel(self)
        pixmap = QPixmap("img/cog-speed.png")
        self.labelMotor.setPixmap(pixmap)
        self.labelMotor.move(35, 227)

        self.numMotor = QLabel(self)
        self.numMotor.setText("100")
        self.numMotor.setStyleSheet("QLabel{ color:#44E4DA; font-size:25px; } ")
        self.numMotor.move(133, 231)


        self.homeBtn = QPushButton(self)
        self.homeBtn.setIcon(QIcon('img/home_btn.png'))
        self.homeBtn.setIconSize(QSize(50,46))
        self.homeBtn.resize(50,46)
        self.homeBtn.move(5, 271)

    def fetch_network(self, msg):

        print ('get MSG : '+msg)
        if msg == 'LEFT':
            pixmap = QPixmap("img/status_left.png")
        elif msg == 'RIGHT':
            pixmap = QPixmap("img/status_right.png")
        elif msg == 'STOP':
            pixmap = QPixmap("img/status_stop.png")
        elif msg == 'load':
            pixmap = QPixmap("img/status_connecting.png")
        else:
            #qstr = QString(msg)
            slist = msg.split("|")
            print (slist[1])
            self.numMotor.setText(slist[1])
            pixmap = QPixmap("img/status_stop.png")


        self.status.setPixmap(pixmap)


def main():
    net = netpie()
    app = QApplication(sys.argv)
    ex = Remote(net)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
