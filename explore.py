##Import public library python-RPi.GPIO
import RPi.GPIO as gpio
##Import public library python-time
import time
##Import public library python-sys
import sys
##Import local library python-sensors: see sensors.py
import sensors
##Import local library python-driveme: see driveme.py
import driveme
##Import public library python-random
import random

##Goal:
##1. Drive vechicle autonomously in "explore" mode.
##2. Call the distance function from the sensors local library to prove it is functioning correctly.
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

##Call the function distance from the local python script sensors.py
sensors.front_distance()

##Define the function autonomy
def autonomy():
##Set the time to run (for actions other than forward)
    tf = 1
##Introduce a variable, x, that will take on a sudorandom value to drive the vechicle in explore mode. x will take on values from 1-7
    x = random.randrange(0, 8)
##Set actions for the vechicle based on the value of x

##Drive forward for 5 seconds if x = 0
    if x == 0:
##Initialise GPIO pins (based on instructions defined in driveme.py)
        driveme.init()
##Drive forward for 5 seconds
        driveme.forward(5)

##Pivot left for tf seconds if x = 1
    elif x == 1:
        driveme.init()
        driveme.pivot_left(tf)

##Pivot right for tf seconds if x = 2
    elif x == 2:
        driveme.init()
        driveme.pivot_right(tf)

##Drive forward and to the left for tf seconds if x = 3
    elif x == 3:
        driveme.init()
        driveme.turn_left_fwd(tf)

##Drive forward and to the right for tf seconds if x = 4
    elif x == 4:
        driveme.init()
        driveme.turn_right_fwd(tf)

##Drive left and reverse for tf seconds if x = 5
    elif x == 5:
        driveme.init()
        driveme.turn_left_rev(tf)

##Drive right and reverse for tf seconds if x = 6
    elif x == 6:
        driveme.init()
        driveme.turn_right_rev(tf)

##Reverse for tf seconds if x = 7
    elif x == 7:
        driveme.init()
        driveme.reverse(tf)

##Run the function autonomy 10 times (generate 10 random iterations of x which will produce 10 movements at random)
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
