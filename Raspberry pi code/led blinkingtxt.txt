import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,0)
time.sleep(100)
GPIO.output(4,1)
GPIO.cleanup()
