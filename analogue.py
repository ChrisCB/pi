import time, signal, sys
import Adafruit_ADS1x15


def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)	# Not sure what this does tbh
#print 'Press Ctrl+C to exit'

ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01	# 16-bit ADC

# Select the gain
# gain = 6144  # +/- 6.144V
#gain = 4096  # +/- 4.096V
gain = 4
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V


# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
adc = Adafruit_ADS1x15.ADS1015()

seconds_between_readings = 5


# Read channel 0 in single-ended mode using the settings above
#volts = adc.readADCSingleEnded(0, gain, sps) / 1000
while True:
	volts = adc.read_adc(0, gain) / 1000
	print("%.6f" % (volts))
	time.sleep(seconds_between_readings)

# To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
#volts = adc.readADCSingleEnded(3, 1024, 860)

