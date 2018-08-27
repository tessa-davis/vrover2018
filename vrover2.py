import RPi.GPIO as gpio
import time

#Goal: Spin wheels forward and reverse
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

rt_fr_fwd = 16
rt_fr_rev = 18
rt_bk_fwd = 36
rt_bk_rev = 38
lft_fr_fwd = 13
lft_fr_rev = 15
lft_bk_fwd = 35
lft_bk_rev = 37

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
    
forward(3)
reverse(3)
