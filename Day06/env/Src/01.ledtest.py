import RPi.GPIO as GPIO
import time

btnPin = 24
count = 0

def click(channel):
	global count
	if (btnPin+1):
		count = count + 1

	print(count)

while(True):
	time.sleep(1)
