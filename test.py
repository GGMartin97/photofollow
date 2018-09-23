from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
pan = 21
tilt = 17
 
GPIO.setup(tilt, GPIO.OUT) # white => TILT
GPIO.setup(pan, GPIO.OUT) # gray ==> PAN
 
def setServoAngle(servo, angle):
    assert angle >=0 and angle <= 180
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.3)
    pwm.stop()
 
if __name__ == '__main__':  
    for i in range (0, 180, 15):
        setServoAngle(pan, i)
        setServoAngle(tilt, i)
     
    for i in range (180, 0, -15):
        setServoAngle(pan, i)
        setServoAngle(tilt, i)
         
    setServoAngle(pan, 100)
    setServoAngle(tilt, 90)    
    GPIO.cleanup()
