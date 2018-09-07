import RPi.GPIO as gpio
import time

#front_sensor_trig is the GPIO pin number that triggers the sensor (GPIO pin configured as output)
#front_sensor_echo is the GPIO pin number that ingests the echo from the sensor

front_sensor_trig = 31
front_sensor_echo = 29

def distance(measure = 'cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(front_sensor_trig, gpio.OUT)
    gpio.setup(front_sensor_echo, gpio.IN)
    
    gpio.output(front_sensor_trig, False)
    while gpio.input(front_sensor_echo) == 0:
        nosig = time.time()
        
    while gpio.input(front_sensor_echo) == 1:
        sig = time.time()
        
    tl = sig - nosig
    
    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print("improper choice of measurement: in or cm")
        distance = None
        
    gpio.cleanup()
    return distance

print(distance('cm'))