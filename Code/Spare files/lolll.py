import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn
conversion_factor = 3.3 / (65535)
pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
ldr1 = AnalogIn(board.GP26)
ldr2 = AnalogIn(board.GP27)
servo1 = servo.Servo(pwm)

while True:
    lightValue = ldr1.value * conversion_factor
    lightValue2 = ldr2.value * conversion_factor
    if lightValue > lightValue2:
        for angle in range(0, 180, 1):
            servo1.angle = angle
            time.sleep(0.05)
    elif lightValue < lightValue2:
        for angle in range (0, 180, -1):
            servo1.angle = angle
            time.sleep(0.05)    
    else:
        for angle in range(180, 0, 0):
            servo1.angle = angle
            time.sleep(0.05)
    
    
  
  

