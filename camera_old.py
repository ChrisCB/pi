#from PIL import Image
#img = Image()


from picamera import PiCamera
from time import sleep

#Define variables
camera = PiCamera()
seconds_between_images = 10
count = 0

while True:
	camera.start_preview(alpha=200)
	sleep(2)
	camera.capture('test.jpg')
	count = count + 1
	print("Took photo")
	camera.stop_preview()
	sleep(seconds_between_images)
	camera.close()
