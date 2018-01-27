import RPi.GPIO as GPIO
import time
print("Testing the moisture level...")

def callback(channel):
	if GPIO.input(channel):
		print("LED on - moist")
	else:
		print("LED off - dry")

# Set GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)
# Define GPIO pin that sensor is connected to
channel = 17
# Set that pin to an iput
GPIO.setup(channel, GPIO.IN)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel,callback)

while True:
	time.sleep(1)
