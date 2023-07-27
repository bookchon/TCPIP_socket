import RPi.GPIO as GPIO
import time

swPin = 6
swLed = 16
swspk = 20
count = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(swLed, GPIO.OUT)
GPIO.setup(swspk, GPIO.OUT)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(swLed, True)
GPIO.setwarnings(False)

siren = GPIO.PWM(swspk, 1.0)
siren.start(90.0)

sir = [523, 262]

def callbackfunc(channel):
	global count
	count = count + 1
	if (count % 2 == 0):
		for i in range(0, 1):
			siren.ChangeFrequency(sir[i])
			GPIO.output(swLed, GPIO.LOW)
	else:
		GPIO.output(swLed, GPIO.HIGH)

	print("Interrupt")
	siren.stop()

GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc)

try:
	while True:
		pass
finally:
	GPIO.cleanup()
