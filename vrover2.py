import RPi.GPIO as gpio
import time

#Goal: Spin wheels forward and reverse
#Colour is the colour on breadboard
#On HBridge, connections are to:
#Assumption: Rt Wheels and Left wheels spin together
#Blue to Input 4 - Right Reverse Spin - right_rev
#Purple to Input 3 - Right Forward Spin - right_fwd
#Grey to Input 2 - Left Forward Spin - left_fwd
#White to Input 1 - Left Reverse Spin - left_rev
#Future work: consider 4 wheel independence

right_rev = 7
right_fwd= 11
left_fwd = 13
left_rev = 15

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(right_rev, gpio.OUT)
    gpio.setup(right_fwd, gpio.OUT)
    gpio.setup(left_fwd, gpio.OUT)
    gpio.setup(left_rev, gpio.OUT)
    
def forward(tf):
    init()
    gpio.output(right_rev, False)
    gpio.output(right_fwd, True)
    gpio.output(left_fwd, True)
    gpio.output(left_rev, False)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    init()
    gpio.output(right_rev, True)
    gpio.output(right_fwd, False)
    gpio.output(left_fwd, False)
    gpio.output(left_rev, True)
    time.sleep(tf)
    gpio.cleanup()
    
forward(3)
reverse(3)
