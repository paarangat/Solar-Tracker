import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn
conversion_factor = 3.3 / (65535)
pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
adcpin = AnalogIn(board.GP26)
my_servo = servo.Servo(pwm)
while True:
    lightValue = adcpin.value * conversion_factor
    angle = (180 / 3.3) * lightValue
    my_servo.angle = angle
    time.sleep(0.2)        
