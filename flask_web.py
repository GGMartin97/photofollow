from flask import Flask,request,render_template
import time
import RPi.GPIO as GPIO
import hello

move1=3
move2=3

app=Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html')


@app.route('/data1')
def data1():
	global move1
	if move1<13 and move1>3:
		move1=move1+1
		hello.tmp1(move1)
	return render_template('index.html')

@app.route('/data2')
def data2():
	global move1
	if move1<13 and move1>3:
		move1=move1-1
		hello.tmp1(move1)
	return render_template('index.html')

@app.route('/data3')
def data3():
	global move2
	if move2<13 and move2>3:
		move2=move2+1
		hello.tmp2(move2)
	return render_template('index.html')

@app.route('/data4')
def data4():
	global move2
	if move2<13 and move2>3:
		move2=move2-1
		hello.tmp2(move2)
	return render_template('index.html')

if __name__==('__main__'):
	app.run(debug=True,port=8000,host='0.0.0.0')
