import RPi.GPIO as gpio
import time
import sys
import sensors
import driveme
import random

#Goal:
##1. Drive vechicle autonomously in "explore" mode.
##2. Check the distance before performing each action and print the result.
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

sensors.front_distance()

def check_front():
    dist = sensors.front_distance()

    if dist < 15:
        print('Too close,',dist)

    else:
        print('Front okay,',dist)

def autonomy():
    tf = 1
    x = random.randrange(0, 8)

    if x == 0:
        check_front()
        driveme.init()
        driveme.forward(3)

    elif x == 1:
        driveme.init()
        driveme.pivot_left(tf)

    elif x == 2:
        check_front()
        driveme.init()
        driveme.pivot_right(tf)

    elif x == 3:
        check_front()
        driveme.init()
        driveme.turn_left_fwd(tf)

    elif x == 4:
        check_front()
        driveme.init()
        driveme.turn_right_fwd(tf)

    elif x == 5:
        check_front()
        driveme.init()
        driveme.turn_left_rev(tf)

    elif x == 6:
        check_front()
        driveme.init()
        driveme.turn_right_rev(tf)

    elif x == 7:
        check_front()
        driveme.init()
        driveme.reverse(tf)

for z in range(10):
    autonomy()



'''def check_front():
    driveme.init()
    dist = sensors.distance()

    if dist < 15:
        print('Too close,',dist)
        driveme.init()
        driveme.reverse(2)
        dist = sensors.distance()
        if dist < 15:
            print('Too close,', dist)
            driveme.init()
            driveme.pivot_left(3)
            driveme.init()
            driveme.reverse(2)
            dist = sensors.distance()
            if dist < 15:
                print('Too close, giving up', dist)
                sys.exit()

def autonomy():
    tf = 2
    x = random.randrange(0, 4)

    if x == 0:
        for y in range(30):
            check_front()
            driveme.init()
            driveme.forward(tf)

    elif x == 1:
        for y in range (30):
            check_front()
            driveme.init()
            driveme.pivot_left(tf)

    elif x == 2:
        for y in range (30):
            check_front()
            driveme.init()
            driveme.turn_right_fwd(tf)

    elif x == 3:
        for y in range (30):
            check_front()
            driveme.init()
            driveme.turn_left_fwd(tf)

for z in range(10):
    autonomy()'''
