import math
from MCP3008 import MCP3008
from mq2 import *
import sys, time
import RPi.GPIO as GPIO
import pyrebase
import smbus
import time
from time import sleep
from datetime import datetime
from datetime import date
import picamera


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #Set GPIO to pin number
BuzzerPin = 5
GPIO.setup(BuzzerPin, GPIO.OUT)
GPIO.output(BuzzerPin, GPIO.HIGH)

pir = 26 #Assign pin 8 to PIR
GPIO.setup(pir, GPIO.IN) #Setup GPIO pin PIR as input
bus = smbus.SMBus(1)
GPIO.setup(22,GPIO.OUT)

def databaseinit():
    
    config = {
        "apiKey": "AIzaSyCVmArWmfshhRhvbyyUAJBqMKQp8UrOT50",
        "authDomain": "smarthomemonitor-65364.firebaseapp.com",
        "databaseURL": "https://smarthomemonitor-65364.firebaseio.com/",
        "storageBucket": "gs://smarthomemonitor-65364.appspot.com/"
        }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    return db

def storageinit():

    config = {
        "apiKey": "AIzaSyCVmArWmfshhRhvbyyUAJBqMKQp8UrOT50",
        "authDomain": "smarthomemonitor-65364.firebaseapp.com",
        "databaseURL": "https://smarthomemonitor-65364.firebaseio.com/",
        "storageBucket": "smarthomemonitor-65364.appspot.com"
        }
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    return storage
    

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()

def beep(rawVal):
    if (rawVal > 600):
        GPIO.output(BuzzerPin, GPIO.LOW)
        time.sleep(0.5)
    else:
        GPIO.output(BuzzerPin, GPIO.HIGH)
        time.sleep(0.5)

def imageCapture():
   
   
    storage = storageinit()
    db = databaseinit()

    print ("Running image capture")
    camera = picamera.PiCamera()
    camera.capture("myimage.jpg")
    time.sleep(3)
    
    

    camera.close()
    storage.child("Images/test.jpg").put("myimage.jpg")
    
    #url = storage.child("images/").get_url("test.jpg")
    #print url

    #db.child("uploads").push(url)
    
def SHT31SensorTemp(cTemp):
    GPIO.output(22,GPIO.HIGH)
    bus.write_i2c_block_data(0x44, 0x2C, [0x06]) 
    time.sleep(0.5)
    data = bus.read_i2c_block_data(0x44, 0x00, 6)
    temp = data[0] * 256 + data[1]
    cTemp = -45 + (175 * temp / 65535.0)
    GPIO.output(22,GPIO.LOW)
    return cTemp

def SHT31SensorHum(humidity):
    GPIO.output(22,GPIO.HIGH)
    bus.write_i2c_block_data(0x44, 0x2C, [0x06]) 
    time.sleep(0.5)
    data = bus.read_i2c_block_data(0x44, 0x00, 6)
    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
    GPIO.output(22,GPIO.LOW)
    return humidity
    
#try:
#print("Press CTRL+C to abort. -Andrew")
mq2 = MQ()
print("Class has been created")
rawVal = 0.0
temp = 0
hum = 0
count = 0

while 1:

    db = databaseinit()
    #db2 = databaseinit()
    #db2.child("Member")
    #newdb = db2.child(("SyidSZhQNuO9rH6P3TnSHIQU41B3").child("Devices").child("Lucas's Room").child("MotionDectection")).get
    #print (newdb)
    
    db.child("Member").child("SyidSZhQNuO9rH6P3TnSHIQU41B3").child("Devices").child("Lucas's Room").child("MotionDectection")

    data = db.child().get()
    print (data.val())
    
   
    if GPIO.input(pir) == True and data.val() == 0: #If PIR pin goes high, motion is detected
        print ("Motion Detected!")
        imageCapture()
        
    
    print("Calling getRaw")
    rawVal = mq2.getRaw(0)
    
    print ("The raw value is: ")
    print (rawVal)
    beep(rawVal)
        
    db.child("Member").child("SyidSZhQNuO9rH6P3TnSHIQU41B3").child("Devices").child("Lucas's Room").child("Gas_Readings").update({"Gas": rawVal})
    sys.stdout.flush()
    if count == 1800:
        temp = int(SHT31SensorTemp(temp))
        print ("Temperature: %.2f C" %temp)
        db.child("Member").child("SyidSZhQNuO9rH6P3TnSHIQU41B3").child("Devices").child("Lucas's Room").child("Temperature_Readings").update({"Temperature": temp})
        sys.stdout.flush()
        hum = int(SHT31SensorHum(hum))
        print ("Humidity: %.2f %%RH" %hum)
        db.child("Member").child("SyidSZhQNuO9rH6P3TnSHIQU41B3").child("Devices").child("Lucas's Room").child("Humidity_Readings").update({"Hum": hum})
        sys.stdout.flush()
        count = 0
        
    count += 1
    #print (count)
    print (" ")
    print ("------------------------------------------------------------------")
    print (" ")
    
    time.sleep(5)
 