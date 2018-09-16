import RPi.GPIO as gpio
import time
import sys
import sensors
import driveme
import random

#Goal: Drive vechicle autonomously using:
## ---sensors.distance() --- Return the distance from the sensor to the nearest object
## ---driveme.init() --- Initialise GPIO pins to drive as output
## ---driveme.forward(tf) --- Drive Foward
## ---driveme.reverse(tf) --- Drive in Reverse
## ---driveme.turn_left_fwd(tf) --- Turn left while moving forward
## ---driveme.turn_right_fwd(tf) --- Turn right while moving forward
## ---driveme.turn_left_rev(tf) --- Turn left while moving backward
## ---driveme.turn_right_rev(tf) --- Turn right while moving backward
## ---driveme.pivot_right(tf) --- Pivot clockwise (defined as from a 'birds eye view' with 12o'clock at the front of the vehicle (Pivot right)
## ---driveme.pivot_left(tf) --- Pivot counter clockwise (Pivot left)

#Assumptions: see driveme.py

def check_front():
    driveme.init()
    dist = sensors.distance()

    if dist < 15:
        print('Too close,',dist)
        init()
        reverse(2)
        dist = sensors.distance()
        if dist < 15:
            print('Too close,', dist)
            init()
            driveme.pivot_left(3)
            init()
            reverse(2)
            dist = sensors.distance()
            if dist < 15:
                print('Too close, giving up', dist)
                sys.exit()

def autonomy():
    tf = 0.030
    x = random.randrange(0, 4)

    if x == 0:
        for y in range(30):
            check_front()
            driveme.init()
            driveme.forward(tf)

    elif x == 1:
        for y in range (30):
            check_front()
            init()
            driveme.pivot_left(tf)

    elif x == 2:
        for y in range (30):
            check_front()
            init()
            driveme.turn_right_fwd(tf)

    elif x == 3:
        for y in range (30):
            check_front()
            init()
            driveme.turn_left_fwd(tf)

for z in range(10):
    autonomy()

