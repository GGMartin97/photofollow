import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


tilt=21

GPIO.setup(tilt,GPIO.OUT)


pwm=GPIO.PWM(tilt,50)

pwm.start(0)

pwm.ChangeDutyCycle(12)

time.sleep(1)

pwm.stop()

GPIO.cleanup()