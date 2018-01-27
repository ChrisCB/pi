import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15

def signal_handler(signal, frame):
	print("You pressed Ctrl + C!")
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

ADS1015 = 0x00
ADS1115 = 0x01

gain = 4096

sps = 8 # Samples per second

ads = ADS1x15(ic=ADS1015)

volts = ads.readADCSingle(0, gain, sps) / 1000

print(volts)