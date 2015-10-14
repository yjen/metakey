import RPi.GPIO as GPIO
import requests
import time

#initialize constants
servo = 18
freq = 50
metakey_server = "http://metakey.meteor.com/api"
key = u'releasing'

#set up pin
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, freq)

pwm.start(10)

def stopMotor():
  pwm.ChangeDutyCycle(10)
  time.sleep(0.1)

try:
  while(True):
    r = requests.get(metakey_server)
    open = r.json()[0][key]
    if(open):
      pwm.ChangeDutyCycle(10)
      time.sleep(0.1)
      pwm.ChangeDutyCycle(12)
      time.sleep(5)
      pwm.ChangeDutyCycle(10)
      time.sleep(0.1)
    time.sleep(5)

except KeyboardInterrupt:
  stopMotor()
  GPIO.cleanup()
