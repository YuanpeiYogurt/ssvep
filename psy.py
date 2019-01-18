from psychopy import visual, core

import numpy as np
import sys
import cv2
import os
import time
#import _thread as thread
#from multiprocessing import Process

rcycles = 14
tcycles = 12
stimSize =128
xylim = 2 * np.pi* rcycles
freq1=7.5
freq2=10
freq3=12
freq4=13
#color variable
white = 180
grey = 100
black = 0
D=10
L=18
pos1 = (256,100)
pos2 = (-256,100)
pos3 = (256,-100)
pos4 = (-256,-100)
#def getFrame(n,freq):
#    #Generate next frame of simulation as numpy array
#    if getFrame.z is None: 
#        #for the meshgrid
#        x2, y2 = np.meshgrid(np.linspace(-xylim,xylim,stimSize), np.linspace(-xylim,xylim,stimSize))
#        #Get the value of the pixel function
#        getFrame.z = circularCheckerBoard(x2, y2,n,freq)      
#    return getFrame.z

def getFrame(n,freq):
    #Generate next frame of simulation as numpy array
    #for the meshgrid
    x1, y1 = np.meshgrid(np.linspace(-xylim,xylim,stimSize), np.linspace(-xylim,xylim,stimSize))
    #Get the value of the pixel function
    #getFrame.z = circularCheckerBoard(x2, y2,n,freq)      
    
    #based on matlab code
    sql = xylim**2
    at = np.arctan2(x1,y1)
    xylim1 = x1
    phiAngle=(np.pi/2)+(np.pi/2)*np.sin((2*np.pi*n*(freq/(2*60)))-(np.pi/2)) 
    checks = np.sign(np.cos((np.pi*np.sqrt(x1**2 + y1**2)/D)+phiAngle*(L/D))*np.cos(at*tcycles))
    circle1 = ((x1**2 + y1**2) <= xylim**2)*1
    circle2 = ((x1**2 + y1**2) >= 30)*1
    checks = checks* circle1* circle2
    
    
    
    return checks

def sin2d(x,y):
    return np.sin(x) + np.cos(y)

def circularCheckerBoard(x1,y1,n,freq):
    #based on matlab code
    sql = xylim**2
    at = np.arctan2(x1,y1)
    xylim1 = x1
    phiAngle=(np.pi/2)+(np.pi/2)*np.sin((2*np.pi*n*(freq/(2*60)))-(np.pi/2)) 
    checks = np.sign(np.cos(np.pi*np.sqrt(x1**2 + y1**2)/D+phiAngle*(L/D))*np.cos(at*tcycles))
    circle1 = ((x1**2 + y1**2) <= xylim**2)*1
    circle2 = ((x1**2 + y1**2) >= 10)*1
    checks = checks* circle1* circle2
    #print(circle)
    return checks



#def proc(freq, posi):
#    for i in range(1,600):
#        # Get a numpy array to display from the simulation
##        getFrame.z = None
#        npimage=getFrame(i,freq)
#        checkerboard = visual.GratingStim(win, tex=npimage,size=(256,256),units='pix')
#        checkerboard.pos = posi
#        checkerboard.draw()
#        win.flip()

if __name__ == '__main__':
#setup stimulus
    win=visual.Window([1024,512])

    clock = core.Clock()
    t0 = time.time()
    
    #thread.start_new_thread(proc, (freq1, pos1) )
#    
#    p1 = Process(target=proc1)
#    p2 = Process(target=proc2)
#    
#    p1.start()
#    p1.join()
#    p2.start()
#    p2.join()
    for i in range(1,4*600):
        npimage1=getFrame(i,freq1)
        checkerboard1 = visual.GratingStim(win, tex=npimage1,size=(128,128),units='pix')
        checkerboard1.pos = pos1        
        npimage2=getFrame(i,freq2)
        checkerboard2 = visual.GratingStim(win, tex=npimage2,size=(256,256),units='pix')
        checkerboard2.pos = pos2
        npimage3=getFrame(i,freq3)
        checkerboard3 = visual.GratingStim(win, tex=npimage3,size=(256,256),units='pix')
        checkerboard3.pos = pos3
        npimage4=getFrame(i,freq4)
        checkerboard4 = visual.GratingStim(win, tex=npimage4,size=(256,256),units='pix')
        checkerboard4.pos = pos4
        checkerboard1.draw()
        checkerboard2.draw()
        checkerboard3.draw()
        checkerboard4.draw()
        win.flip()
    t1 = time.time()    
    print(t1-t0)

