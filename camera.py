# Every 12 hours take a photo
# Save it to a folder within the project
# Extract the G from the RGB
# Write the G value to a two dimensional array
# results = [[1,0.1],[2,0.2],[3.0.25]]
# Delete the photo

import time
from picamera import PiCamera
import random 	# temp. Delete when CV working

seconds_between_images = 10	#image frequency
count = 0
camera = PiCamera()
camera.resolution = (1280,720)
results = []

def find_green(count):
	green = random.uniform(0,1) # Temp until CV works
	when = time.strftime("%Y-%m-%d %H:%M:%S")
	results.append([count,when,green])
	print(results[-1])
	return results
	

while True:
	camera.start_preview()
	time.sleep(2) #Time to warm up camera
	camera.capture('test_2.jpg')
	count = count + 1
	print("got picture number " + str(count))
	camera.stop_preview()
	camera.close
	find_green(count) # pass in image
	time.sleep(seconds_between_images) #image frequency
	# now delete the image







