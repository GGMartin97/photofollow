import RPi.GPIO as GPIO
import time

def tmp1(tilt1):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings=False
	GPIO.setup(20,GPIO.OUT)
	pwm=GPIO.PWM(20,50)
	pwm.start(0)
	pwm.ChangeDutyCycle(tilt1)
	time.sleep(0.5)
	pwm.stop()
	GPIO.cleanup()

def tmp2(tilt2):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings=False
	GPIO.setup(21,GPIO.OUT)
	pwm=GPIO.PWM(21,50)
	pwm.start(0)
	pwm.ChangeDutyCycle(tilt2)
	time.sleep(0.5)
	pwm.stop()
	GPIO.cleanup()
