import time
import picamera

image = "images/camera_still_%s.jpg" % time.strftime("%Y-%m-%d %H:%M")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(120)
    camera.capture(image)
