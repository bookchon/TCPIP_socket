import RPi.GPIO as GPIO
import time

swPin = 6
swLed = 16
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(swLed, GPIO.OUT)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(swLed, True)
GPIO.setwarnings(False)

def callbackfunc(channel):
	global count
	count = count + 1
	if (count % 2 == 0 ):
		GPIO.output(swLed, GPIO.LOW)
	else:
		GPIO.output(swLed, GPIO.HIGH)
	print("Interrupt")

GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
