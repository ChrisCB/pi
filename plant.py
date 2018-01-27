import picamera
import picamera.array
import csv
import time
import signal
import sys
import Adafruit_ADS1x15

from pump import auto_water


# 1 Define variables
seconds_between_readings = 1800		# Reading frequency - 3600 seconds p/h
count = 0
results = []
output_file_name = "results/plant_output %s.csv" % time.strftime("%Y-%m-%d %H:%M")


# 1.1 sMoisture sensor variables
ADS1015 = 0x00  # 12-bit ADC
gain = 4
adc = Adafruit_ADS1x15.ADS1015()	# Initialise the ADC using the default mode (use default I2C address)


# 2 Setup CSV file for output
with open(output_file_name,'a') as file:
	file.write("Reading, Time, Green_Value, Red_Value, Blue_Value, Green_Percent, Volts - Higher is drier, Water Dispensed')                                                                                                                                                                         ")

def write_result_csv(count,when,green,red,blue,green_percent,volts,water_dispensed):
	with open(output_file_name,'a') as file:
		file.write("\n" + count + "," + when + "," + green + "," + red + "," + blue + "," + g_percent + "," + volts + "," + water_dispensed)

# 3 Output some details to the screen
print("Taking readings every %s seconds" % seconds_between_readings)
print("Saving results to: %s" % output_file_name)
print('| Reading | Time | Green | Green % | Volts (Moisture. Higher is Drier) | Water Dispensed?')

# 4 The actual loop
try:
	while True:
		water_dispensed = 'No water'				# Reset to no water by default
		with picamera.PiCamera() as camera:
			with picamera.array.PiRGBArray(camera) as output:
				camera.capture(output, 'rgb')
				red = output.array[:, :, 0].mean()
				green = output.array[:, :, 1].mean()
				blue = output.array[:, :, 2].mean()
				total = red + green  + blue
				if total == 0:						# Catch divide by zero. Prob a better way to do this.
					total = 0.0000000001
				g_percent = str(round(green / (total),2))
			camera.close()
			
			# Moisture
			volts = adc.read_adc(0, gain) / 1000	# Lower = wetter
			
			if volts > 2.1:						# Make this dynamic somehow
				auto_water()
				water_dispensed = 'water'
			
			# Meta-data
			count = count + 1
			when = time.strftime("%Y-%m-%d %H:%M:%S")
		
			# Results
			results.append([count,when,green,g_percent,volts, water_dispensed])
			write_result_csv(str(count), str(when), str(round(green,2)), str(round(red,2)), str(round(blue,2)), str(g_percent), str(volts), water_dispensed)
			print(results[-1])
			
			time.sleep(seconds_between_readings)

except KeyboardInterrupt:
	print("Keyboard interrupt - tidying up")
	camera.close()
		
