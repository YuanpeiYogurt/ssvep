import numpy as np
import sys
import cv2
import os
import time

rcycles = 14;
tcycles = 12;
stimSize = 250;
xylim = 2 * np.pi* rcycles;
freq=3;
numFrames=120/freq;
#color variable
white = 200
grey = 100
black = 0
D=10
L=20

    
def getFrame(n):
    #Generate next frame of simulation as numpy array
    if getFrame.z is None: 
        #for the meshgrid
        x2, y2 = np.meshgrid(np.linspace(-xylim,xylim,stimSize-1), np.linspace(-xylim,xylim,stimSize-1))
        #x2, y2 = np.meshgrid(np.linspace(-xylim,xylim,(0.5*xylim/(stimSize-1))), np.linspace(-xylim,xylim,0.5*xylim/(stimSize-1)))
        #Get the value of the pixel function
        
        #t0 = time.time()
        getFrame.z = circularCheckerBoard(x2, y2,n)
        
        #t1 = time.time()
        #print(t1 - t0, "seconds wall time\n")   
        
    return getFrame.z

def sin2d(x,y):
    return np.sin(x) + np.cos(y)

def circularCheckerBoard(x1,y1,n):
    #based on matlab code
    sql = xylim**2
    at = np.arctan2(x1,y1)
    xylim1 = x1
    phiAngle=(np.pi/2)+(np.pi/2)*np.sin((2*np.pi*n*(freq/(2*60)))-(np.pi/2)) 
    checks = np.sign(np.cos(np.pi*np.sqrt(x1**2 + y1**2)/D+phiAngle*(L/D))*np.cos(at*tcycles))
    circle = ((x1**2 + y1**2) <= xylim**2)*1
    checks = checks* circle
    #print(circle)
    return checks


getFrame.z = None
t0 = time.time()
for i in range(1,600):
    
    
     
    # Get a numpy array to display from the simulation
    getFrame.z = None
    npimage=getFrame(i)

    cv2.imshow('image',npimage)
    #cv2.waitKey(round(1000/60))
    cv2.waitKey(1)
    time.sleep(1./60)

t1 = time.time()
print(t1 - t0, "seconds wall time\n")    
import os
os._exit(1)