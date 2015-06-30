# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import atan, pi, degrees

def sensortoradial(NW, NE, SE, SW):
    
    Y = ((NE + NW)/2) - ((SE + SW)/2)
    X = ((NE + SE)/2) - ((NW + SW)/2)
    
    print Y, X
    try:
        intensity = (X**2 + Y**2)**(0.5)
        acardinal = abs(atan(Y/X))
    except ZeroDivisionError:
        acardinal = 90
    
    
    print acardinal
    
    if Y > 0 and X > 0:
        cardinal = degrees(acardinal) #quadrant 1 math
    elif Y > 0 and X < 0:
        cardinal = degrees(pi - acardinal) #quadrant 2 math
    elif Y < 0 and X < 0:
        cardinal = degrees(pi + acardinal) #quadrant 3 math
    elif Y < 0 and X > 0:
        cardinal = degrees(pi * 2 - acardinal) #quadrant 4 math
    elif X == 0 and Y > 0:
        cardinal = 90
    elif X == 0 and Y < 0:
        cardinal = 270
    elif Y == 0 and X > 0:
        cardinal = 0
    elif Y == 0 and X < 0:
        cardinal = 180
    elif Y == 0 and X == 0:
        return 0, 0
    else:
        raise ValueError("this is all fucked up")
    
    truecard = (-(cardinal-90)) % 360
    
    return intensity, truecard

while True:
    
    try:
        NW = float(raw_input())
        NE = float(raw_input())
        SE = float(raw_input())
        SW = float(raw_input())
    
    except ValueError:
        print "analog inputs must be integers"
        continue
    
    print NW, NE, SE, SW
    break

values = sensortoradial(NW, NE, SE, SW)
        
print "Intensity is: %f in the direction of: %f" %values
