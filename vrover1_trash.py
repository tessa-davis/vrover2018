import RPi.GPIO as gpio
import time

#Goal: Spin 4 wheels in one direction (forward)
#Colour is the colour on breadboard
#On HBridge, connections are to:
#Blue to Input 4
#Purple to Input 3
#Grey to Input 2
#White to Input 1
#Future work: replace colour in variable name with wheel location

blue = 7
purple = 11
grey = 13
white = 15

gpio.setmode(gpio.BOARD)

gpio.setup(blue, gpio.OUT)
gpio.setup(purple, gpio.OUT)
gpio.setup(grey, gpio.OUT)
gpio.setup(white, gpio.OUT)

gpio.output(blue, True)
gpio.output(purple, True)
gpio.output(grey, True)
gpio.output(white, True)

time.sleep(5)

gpio.cleanup()
