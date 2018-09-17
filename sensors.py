##Import the GPIO library
import RPi.GPIO as gpio
##Import the time library
import time

##front_sensor_trig is the GPIO pin number that triggers the sensor (GPIO pin configured as output)
##front_sensor_echo is the GPIO pin number that ingests the echo from the sensor

##front_sensor_trig = 31
##front_sensor_echo = 29

print("Distance Measurement in Progress")

##Define the distance function (to be imported into drive script)
def front_distance():

##Define the GPIO pin number connected to trig
    front_sensor_trig = 31
##Define the GPIO pin number connected to echo
    front_sensor_echo = 29

##Set the gpio mode to "board" as opposed to BCM to use the physical pin numbers
    gpio.setmode(gpio.BOARD)
##Set up pins for trig (out of RPi, into sensor) and echo (out of sensor, in to RPi)
    gpio.setup(front_sensor_trig, gpio.OUT)
    gpio.setup(front_sensor_echo, gpio.IN)

##Making sure that the output pin has no pre-configured value
    gpio.output(front_sensor_trig, False)
##Print out notice that the sensor is initiating
    print("Waiting for sensor to settle")
##Give the sensor time to come online
    time.sleep(2)

##Trigger the sensor (8 ultrasound bursts at 40 kHz)
    gpio.output(front_sensor_trig, True)
##Confiture the length of the burst to 10uS
    time.sleep(0.00001)
##Stop the burst after 10uS
    gpio.output(front_sensor_trig, False)


##Listen on the echo pin and as long as there is no signal, take a time stamp (time.time())
    while gpio.input(front_sensor_echo) == 0:
        pulse_start = time.time()
##Take a time stamp of the last recorded moment of a high signal
    while gpio.input(front_sensor_echo) == 1:
        pulse_end = time.time()
##Pulse_duration is the time that passed between a signal appearing and disappearing
    pulse_duration = pulse_end - pulse_start


##The speed of sound in air at sea level = 343m/s or 34 300cm/s
##s = d/t : d = s*t. The sound travels to the object and back so d = (s*t)/2
    front_distance = 17150 * pulse_duration
##Return an answer to 2 decimal places
    front_distance = round(front_distance, 2)

##Clen up the GPIO pins
    gpio.cleanup()

##Instruct the function to return 'distance'
    return front_distance

print front_distance(), "cm"
