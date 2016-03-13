#!/usr/bin/python
# -*- coding: utf-8 -*-



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

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("img/logo_menu.png")

        lbl = QtGui.QLabel(self)
        lbl.move(100,100)
        lbl.setPixmap(pixmap)
        
        b2 = QPushButton(self)
        b2.setText("Button2")
        b2.move(50,50)

        hbox.addWidget(lbl)
       
        self.setLayout(hbox)

        self.move(0,0)
        self.resize(480, 320)
        self.setWindowTitle('DollyProject')
        self.show()        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    