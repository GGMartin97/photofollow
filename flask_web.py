from flask import Flask,request,render_template
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

tilt1=21
tilt2=20
GPIO.setup(tilt2,GPIO.OUT)
GPIO.setup(tilt1,GPIO.OUT)
pwm1=GPIO.PWM(tilt1,50)
pwm2=GPIO.PWM(tilt2,50)
pwm1.start(0)
pwm2.start(0)
move1=3
move2=3

app=Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html')


@app.route('data1')
def data1():
	global move1
	if move1<13||move1>3:
		move1=move1+1
	pwm1.ChangeDutyCycle(move1)

@app.route('data2')
def data1():
	global move1
	if move1<13||move1>3:
		move1=move1-1
	pwm1.ChangeDutyCycle(move1)

@app.route('data3')
def data1():
	global move2
	if move2<13||move2>3:
		move2=move2+1
	pwm2.ChangeDutyCycle(move2)

@app.route('data4')
def data1():
	global move2
	if move2<13||move2>3:
		move2=move2-1
	pwm2.ChangeDutyCycle(move2)