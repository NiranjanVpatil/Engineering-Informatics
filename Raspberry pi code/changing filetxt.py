print("welcome to reverse parking system")
import RPi.GPIO as GPIO  
import time
from time import sleep
                                     
GPIO.setmode(GPIO.BOARD)              #GPIO Mode (BOARD / BCM)
                                      #set GPIO Pins and buzzer 
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
def distance():

    
    GPIO.output(GPIO_TRIGGER, True)   # set Trigger to HIGH

   
    time.sleep(0.5)                   # set Trigger after 0.5s to LOW

    GPIO.output(GPIO_TRIGGER, False)
  
    StartTime = time.time()
    StopTime = time.time()

    
    while GPIO.input(GPIO_ECHO) == 0:  # save StartTime
        StartTime = time.time()

   

    while GPIO.input(GPIO_ECHO) == 1:   # save time of arrival

        StopTime = time.time()

    

    TimeElapsed = StopTime - StartTime #time diff. between start and arrival

    # multiply with the sonic speed (34300 cm/s)

    # and divide by 2, because front and back

    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':   #function outside

    try:

        while True:

            dist = distance()
            if (dist >2 and dist <100):
                print ("Measured Distance = %.1f cm" % dist) 
                GPIO.output(16,True)
                print(" LED  Glow. ")
               
                
            else:
                print(" out of range ")
                GPIO.output(16,False)
                print(" LED Does Not Glow. ")
                time.sleep(1)
                
    except KeyboardInterrupt:  # Reset by pressing CTRL + C
          print("Measurement stopped by User")

GPIO.cleanup()
exit()
                                                                                                                                                                           
