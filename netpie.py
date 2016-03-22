import microgear.client as client
import time


gearkey = 'K0v7QsvD5AgzE0n'
gearsecret =  'tGEE3SdcIpo2sDfzx3mHqKcm4Jd92s'
appid = 'DollyProject'

client.create(gearkey,gearsecret,appid)

def connection():
    print "Now I am connected with netpie"

def subscription(topic,message):
    print topic+" "+message

client.setname("remote")
client.setalias("raspberrypi")
client.on_connect = connection
client.on_message = subscription
client.subscribe("/remote2")

client.connect(True)
