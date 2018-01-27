import picamera
import picamera.array
import time
import csv

#Define variables
seconds_between_images = 60	#image frequency - 3600 seconds p/h
count = 0
results = []
output_file_name = "results/vis_output %s.csv" % time.strftime("%Y-%m-%d %H:%M")

# Setup CSV file for output
with open(output_file_name,'a') as file:
	file.write("Reading, Time, Green_Value")

def write_result_csv(count,when,green):
	with open(output_file_name,'a') as file:
		file.write("\n" + count + "," + when + "," + green "," + red "," + blue, "," + g_percent)

# The actual loop
try:
	while (count < 1000000):			# Temporary limit to stop conflicts
		with picamera.PiCamera() as camera:
			with picamera.array.PiRGBArray(camera) as output:
				camera.capture(output, 'rgb')
				red = output.array[:, :, 0].mean()
				green = output.array[:, :, 1].mean()
				blue = output.array[:, :, 2].mean()
				g_percent = (red + blue) / green
			camera.close()
			
			# Meta-data
			count = count + 1
			when = time.strftime("%Y-%m-%d %H:%M:%S")
			
			# Results
			results.append([count,when,green,g_percent])
			write_result_csv(str(count),str(when),str(round(green,2)), str(round(red,2)), str(round(blue,2)), str(round(g_percent,2))), 
			print(results[-1])
			time.sleep(seconds_between_images)

except KeyboardInterrupt:
	print("Keyboard interrupt - tidying up")
	camera.close()
		
