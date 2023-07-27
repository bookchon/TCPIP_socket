import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 8
ECHO = 7
siren = 20
print("초음파 거리 측정기")

GPIO.setup(TRIG, False)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(siren, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(TRIG, False)
print("초음파 출력 초기화")
time.sleep(2)

sir = GPIO.PWM(siren, 1.0)
sir.start(90.0)

sir = [523]

try:
	while True:
		if (distance < 7):
			siren.ChangeFrequency(sir)
			GPIO.output(TRIG, True)
			time.sleep(0.00001)
		else:
			GPIO.output(TRIG, False)

		while GPIO.input(ECHO) == 0:
			start = time.time()

		while GPIO.input(ECHO) == 1:
			stop = time.time()

		check_time = stop - start
		distance = check_time * 34300 / 2
		print("Distance: %.1f cm" % distance)
		time.sleep(0.4)

except KeyboardInterrupt:
	print("거리 측정 완료")
	GPIO.cleanup()
