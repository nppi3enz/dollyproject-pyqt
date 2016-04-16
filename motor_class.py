from PyQt4.QtCore import *
import time
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

class motor(QThread):

    def __init__(self):
        self.mySpeed = 100

        #print ("initial motor at "+str(mySpeed))
        print ("initial motor at "+str(self.mySpeed))

        self.mh = Adafruit_MotorHAT(addr=0x60)
        atexit.register(self.turnOffMotors)
        self.myMotor_front = self.mh.getMotor(3)
        #self.myMotor_front.setSpeed(mySpeed)

    def turnOffMotors(self):
        print "Off Motor Complete"
    	self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    	self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    	self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    	self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    def left(self):
        self.myMotor_front.run(Adafruit_MotorHAT.FORWARD)
        print "\tSpeed up...to"+str(self.mySpeed)
        self.myMotor_front.setSpeed(self.mySpeed)
        time.sleep(0.01)

    def right(self):
        self.myMotor_front.run(Adafruit_MotorHAT.BACKWARD)
        print "\tSpeed up...to"+str(self.mySpeed)
        self.myMotor_front.setSpeed(self.mySpeed)
        time.sleep(0.01)

    def stop(self):
        self.turnOffMotors()

    def setmySpeed(self, speed):
        self.turnOffMotors()
        print ("new set speed = "+str(speed))
        #self.mySpeed = speed
        self.mySpeed = int(speed)
