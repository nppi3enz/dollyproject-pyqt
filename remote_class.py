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
        self.create_client()
        #self.start_connect()


    def create_client(self):
       gearkey = 'K0v7QsvD5AgzE0n'
       gearsecret =  'tGEE3SdcIpo2sDfzx3mHqKcm4Jd92s'
       appid = 'DollyProject'
       client.create(gearkey,gearsecret,appid)

    def start_connect(self):
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
        print 'Now I am connected with netpie (console)'
        self.mySignal.emit('Now I am connected with netpie')

    def disconnect(self):
        print 'Disconnected!!'

    def subscription(self,topic,message):
        print topic+" "+message
        self.mySignal.emit(message)

    def welcome(self):
        print 'Welcome to NETPIE'


class Remote_Class(QWidget):
    def __init__(self, net):
        super(Remote_Class, self).__init__()
        self.create_main_frame()
        self.net = net
        self.net.mySignal.connect(self.toLog)
        #self.create_client()

    def create_main_frame(self):

        self.cw = QWidget(self)
        self.doit_button = QPushButton('Do it!')
        self.doit_button.clicked.connect(self.on_doit)
        #self.connect(self.doit_button, SIGNAL("testcall()"), self.netpie_console)
        self.discon_button = QPushButton('Disconnect')
        self.discon_button.clicked.connect(self.on_doit)

        #self.log_widget = LogWidget()


        hbox = QHBoxLayout()
        self.listWidget = QListWidget()
        hbox.addWidget(self.doit_button)
        hbox.addWidget(self.discon_button)
        hbox.addWidget(self.listWidget)
        #hbox.addWidget(self.log_widget)

        main_frame = QWidget(self)
        main_frame.setLayout(hbox)


        self.setGeometry(0,0,480,320)
        self.setWindowTitle('DollyProject')
        self.show()

    def create_timer(self):
        self.circle_timer = QTimer(self)
        self.circle_timer.timeout.connect(self.circle_widget.next)
        self.circle_timer.start(25)

    def on_doit(self):
        #self.log('Connecting...')
        self.toLog('Connecting')

        #server = netpie()
        #toLog = self.toLog
        #server.start_connect()
        self.net.start_connect()
        #self.connect(server, SIGNAL(server.start_connect()), toLog, SLOT(server.connection()));
        #server.mySignal.connect(self.test)
        #self.netpie.connect(self.start_connect)
    def disconnect_doit(self):
        server = netpie()
        server.disconnect()


        #self.emit(SIGNAL(self.netpie_console.start_connect()))
    def toLog(self, msg):
        self.listWidget.addItem(msg);

    def test(self):
        print 'testtest'


def main():
    net = netpie()
    app = QApplication(sys.argv)
    ex = Remote_Class(net)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
