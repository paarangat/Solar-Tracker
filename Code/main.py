import time
import board
import digitalio
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn

pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50) #servo setup
adcpin = AnalogIn(board.GP26)
adcpin2 = AnalogIn(board.GP27) 
my_servo = servo.Servo(pwm)
angle = 45   #starting point
 
while True:
    lightValue = adcpin.value
    lightValue2 = adcpin2.value
 
    if lightValue2 > lightValue:
        angle = angle + 1
 
    elif lightValue2 < lightValue:
        angle = angle - 1
     
    if angle > 90:
        angle = 90
         
    if angle < 0:
        angle = 0

    my_servo.angle = angle
    time.sleep(0.02)