import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

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
    
##Define a function that will drive the vechicle forward and left for an amount of time (tf)
def turn_left_fwd(tf):
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
    
##Define a function that will pivot the vechicle clockwise (right) for an amount of time (tf)
def pivot_right(tf):
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


def key_input(event):
    init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time = 1
    
    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        turn_left_fwd(sleep_time)
    elif key_press.lower() == 'd':
        turn_right_fwd(sleep_time)
    elif key_press.lower() == 'q':
        pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)
    elif key_press.lower() == 'z':
        turn_left_rev(sleep_time)
    elif key_press.lower() == 'c':
        turn_right_rev(sleep_time)
    else:
        pass
        
print("""
FEvR11 waiting for directions:

'w': forward 1 second
's': reverse 1 second
'a': turn_left_fwd 1 second
'd': turn_right_fwd 1 second
'q': pivot_left 1 second
'e': pivot_right 1 second
'z': turn_left_rev 1 second
'c': turn_right_rev 1 second

Your input:

""")
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
