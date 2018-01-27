# External module imp
import RPi.GPIO as GPIO
import time

init = False

water_burst_length = 2
delay = 3	# in case a delay is required - 3 seconds

GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
      
def get_status(pin = 8):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
def auto_water(delay = 3, pump_pin = 8):
	init_output(pump_pin)
	bursts = 1
	print("Pump running! Press CTRL+C to exit")
	try:
		while (bursts < 3):
			time.sleep(delay)
			pump_on(pump_pin, 1)
			time.sleep(1)
			bursts = bursts + 1
	
	except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
		GPIO.cleanup() # cleanup all GPI

def pump_on(pump_pin = 8, delay = 5):
    init_output(pump_pin)
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(water_burst_length)
    GPIO.output(pump_pin, GPIO.HIGH)




