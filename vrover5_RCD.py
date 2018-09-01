import RPi.GPIO as gpio
import time

##Goal: Drive vechicle using Remote Control including:
## ---Drive Foward
## ---Drive in Reverse
## ---Turn left while moving forward
## ---Turn right while moving forward
## ---Turn left while moving backward
## ---Turn right while moving backward
## ---Pivot clockwise (defined as from a 'birds eye view' with 12o'clock at the front of the vehicle (Pivot right)
## ---Pivot counter clockwise (Pivot left)

#Assumption: 4 Wheel Independence
#Refer to test image - colour is lead colour. GPIO input defined in variables:
#Blue Lead goes to right front wheel- forward spin (rt_fr_fwd) - green LED
#White lead goes to right front wheel- reverse spin (rt_fr_rev) - red LED
#Pink lead goes to right back wheel- forward spin (rt_bk_fwd) - green LED
#Grey lead goes to right back wheel- reverse spin (rt_fr_rev) - red LED
#Purple Lead goes to left front wheel- forward spin (lft_fr_fwd) - yellow LED
#Yellow lead goes to left front wheel- reverse spin (lft_fr_rev) - red LED
#Green lead goes to left back wheel- forward spin (lft_bk_fwd) - yellow LED
#Orange lead goes to left back wheel- reverse spin (lft_fr_rev) - red LED

##Define variables for each wheel to map to the GPIO pin output. Replace variables with the corresponding GPIO pin on your rover.
rt_fr_fwd = 16
rt_fr_rev = 18
rt_bk_fwd = 36
rt_bk_rev = 38
lft_fr_fwd = 13
lft_fr_rev = 15
lft_bk_fwd = 35
lft_bk_rev = 37

##Set up GPIO pins as output
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(rt_fr_fwd, gpio.OUT)
    gpio.setup(rt_fr_rev, gpio.OUT)
    gpio.setup(lft_fr_fwd, gpio.OUT)
    gpio.setup(lft_fr_rev, gpio.OUT)
    gpio.setup(rt_bk_fwd, gpio.OUT)
    gpio.setup(rt_bk_rev, gpio.OUT)
    gpio.setup(lft_bk_fwd, gpio.OUT)
    gpio.setup(lft_bk_rev, gpio.OUT)

##Define a function that will drive the vechicle forward for an amount of time (tf)
def forward(tf):
    init()
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fr_fwd, True)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, True)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, True)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, True)
    gpio.output(lft_bk_rev, False)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle in reverse for an amount of time (tf)
def reverse(tf):
    init()
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, True)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, True)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, True)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, True)
    time.sleep(tf)
    gpio.cleanup()

##Test drive forward for 3 seconds
#forward(3)
##Test drive in reverse for 3 seconds
#reverse(3)
    
##Define a function that will drive the vechicle forward and left for an amount of time (tf)
def turn_left_fwd(tf):
    init()
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fr_fwd, True)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, True)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, False)

    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_fwd(tf):
    init()
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, True)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, True)
    gpio.output(lft_bk_rev, False)
    time.sleep(tf)
    gpio.cleanup()

##Define a function that will drive the vechicle in reverse and left for an amount of time (tf)
def turn_left_rev(tf):
    init()
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, True)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, True)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, False)

    time.sleep(tf)
    gpio.cleanup()
    
##Define a function that will drive the vechicle forward and right for an amount of time (tf)
def turn_right_rev(tf):
    init()
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, True)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, True)
    time.sleep(tf)
    gpio.cleanup()
    
##turn vehicle left while moving forward for 1 second
#turn_left_fwd(1)
##turn vehicle right while moving forward for 1 second
#turn_right_fwd(1)
##turn vehicle left while reversing for 1 second
#turn_left_rev(1)
##turn vehicle right while reversing for 1 second
#turn_right_rev(1)
    
##Define a function that will pivot the vechicle clockwise (right) for an amount of time (tf)
def pivot_right(tf):
    init()
    gpio.setmode(gpio.BOARD)
    gpio.output(rt_fr_fwd, False)
    gpio.output(rt_fr_rev, True)
    gpio.output(lft_fr_fwd, True)
    gpio.output(lft_fr_rev, False)
    gpio.output(rt_bk_fwd, False)
    gpio.output(rt_bk_rev, True)
    gpio.output(lft_bk_fwd, True)
    gpio.output(lft_bk_rev, False)
    time.sleep(tf)
    gpio.cleanup()

##Define a function that will pivot the vechicle counter-clockwise (left) for an amount of time (tf)
def pivot_left(tf):
    init()
    gpio.output(rt_fr_fwd, True)
    gpio.output(rt_fr_rev, False)
    gpio.output(lft_fr_fwd, False)
    gpio.output(lft_fr_rev, True)
    gpio.output(rt_bk_fwd, True)
    gpio.output(rt_bk_rev, False)
    gpio.output(lft_bk_fwd, False)
    gpio.output(lft_bk_rev, True)
    time.sleep(tf)
    gpio.cleanup()
    
#Pivot vehicle clockwise (right) for 1 second
pivot_right(1)
#Pivot vehicle counterclockwise (left) while moving forward for 1 second
pivot_left(1)

    
