import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn

conversion_factor = 3.3 / (65536)

pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
ldr1 = AnalogIn(board.GP26)
ldr2 = AnalogIn(board.GP27)
ldr3 = AnalogIn(board.GP28)

servo1 = servo.Servo(pwm)

while True:
    lightValue = ldr1.value * conversion_factor
    lightValue2 = ldr2.value * conversion_factor
    lightValue3 = ldr3.value * conversion_factor
    avg1 = (lightValue+lightValue2)/2
    avg2 = (lightValue+lightValue3)/2
    avg3 = (lightValue2+lightValue3)/2
    
    if avg1 > avg2:
        for angle in range(0, 180, 1):
            servo1.angle = angle
            time.sleep(0.05)
    elif avg2 > avg1:
        for angle in range (0,180 -1):
            servo1.angle = angle
            time.sleep(0.05)
    else:
        for angle in range (0,180, 0):
            servo1.angle = angle
            time.sleep(0.05)
            
    if avg2 > avg3:
        for angle in range(0, 180, 1):
            servo1.angle = angle
            time.sleep(0.05)
    elif avg3 > avg2:
        for angle in range (0,180 -1):
            servo1.angle = angle
            time.sleep(0.05)
    else:
        for angle in range (0,180, 0):
            servo1.angle = angle
            time.sleep(0.05)
    
    if avg1 > avg3:
        for angle in range(0, 180, 1):
            servo1.angle = angle
            time.sleep(0.05)
    elif avg3 > avg1:
        for angle in range (0,180 -1):
            servo1.angle = angle
            time.sleep(0.05)
    else:
        for angle in range (0,180, 0):
            servo1.angle = angle
            time.sleep(0.05) 
    
        
    
  
  



    
        
    
  
  



