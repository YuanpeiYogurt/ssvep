import numpy as np
import sys
import cv2
import os
import time

rcycles = 14;
tcycles = 12;
stimSize = 45;
xylim = 2 * np.pi* rcycles;
freq=10;
numFrames=120/freq;
#color variable
white = 200
grey = 100
black = 0
D=10
L=18

    
def getFrame(n):
    #Generate next frame of simulation as numpy array
    if getFrame.z is None: 
        #for the meshgrid
        xx, yy = np.meshgrid(np.linspace(-xylim,xylim,stimSize*4), np.linspace(-xylim,xylim,stimSize*4))
        #Get the value of the pixel function
        getFrame.z = circularCheckerBoard(xx, yy,n)
    return getFrame.z

def sin2d(x,y):
    return np.sin(x) + np.cos(y)

def circularCheckerBoard(xxx,yyy,n):
    #based on matlab code
    sql = xylim**2
    at = np.arctan2(xxx,yyy)
    xylim1 = xxx
    phiAngle=(np.pi/2)+(np.pi/2)*np.sin((2*np.pi*n*(freq/(2*60)))-(np.pi/2)) 
    checks = np.sign(np.cos(np.pi*np.sqrt(xxx**2 + yyy**2)/D+phiAngle*(L/D))*np.cos(at*tcycles))
    circle = ((xxx**2 + yyy**2) <= xylim**2)*1
    checks = checks* circle
    #print(circle)
    return checks


getFrame.z = None

for i in range(1,100):

    # Get a numpy array to display from the simulation
    getFrame.z = None
    npimage=getFrame(i)

    cv2.imshow('image',npimage)
    cv2.waitKey(round(1000/60))
    #time.sleep(1/60)
    

import os
os._exit(1)