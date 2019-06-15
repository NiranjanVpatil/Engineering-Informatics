import RPi.GPIO as GPIO
import time
from time import sleep
buzztime=0.1
buzzerpin=4
buzzerdelay=1
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerpin,GPIO.OUT)
while True:
      print("buzz")
      GPIO.output(buzzerpin,True)
      sleep(buzztime)
      GPIO.output(buzzerpin,False)
      sleep(buzzerdelay)
      GPIO.output(buzzerpin,True)
      sleep(buzztime)
GPIO.cleanup()
exit()
  
