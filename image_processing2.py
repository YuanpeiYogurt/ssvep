import numpy as np
import sys
import cv2
import os
import time
import pygame
#import keyboard

rcycles = 14;
tcycles = 12;
stimSize =250;
xylim = 2 * np.pi* rcycles;
freq=10;
#color variable
white = 200
grey = 100
black = 0
D=10
L=18

pygame.init()

window = (stimSize,stimSize)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

    
def getFrame(n):
    #Generate next frame of simulation as numpy array
    if getFrame.z is None: 
        #for the meshgrid
        x2, y2 = np.meshgrid(np.linspace(-xylim,xylim,stimSize), np.linspace(-xylim,xylim,stimSize))
        #Get the value of the pixel function
        
        getFrame.z = circularCheckerBoard(x2, y2,n)
        

        
    return getFrame.z

def sin2d(x,y):
    return np.sin(x) + np.cos(y)

def circularCheckerBoard(x1,y1,n):
    #based on matlab code
    sql = xylim**2
    at = np.arctan2(x1,y1)
    xylim1 = x1
    phiAngle=(np.pi/2)+(np.pi/2)*np.sin((2*np.pi*n*(freq/(4*60)))-(np.pi/2)) 
    
    checks = np.sign(np.cos(np.pi*np.sqrt(x1**2 + y1**2)/D+phiAngle*(L/D))*np.cos(at*tcycles))

    circle = ((x1**2 + y1**2) <= xylim**2)*1
    checks = checks* circle
    #print(circle)
    return checks


getFrame.z = None

#keyboard.read_key()



#t0 = time.time()
#clock = pygame.time.Clock()
clock = pygame.time.Clock()
t2 = time.time()
for i in range(1,600):
    
    #set fps, which kinda work
    
    #clock.tick(60)
    #print(clock.tick_busy_loop(60))
    #clock.tick()
    #print(clock.get_fps())
    # Get a numpy array to display from the simulation
    getFrame.z = None
    npimage=getFrame(i)
    #print(np.shape(npimage))
    
    pygame.surfarray.blit_array(screen,npimage)
    
    #print(t1 - t0, "seconds wall time\n")       
    
    #screen.blit(background, (0, 0)) 
    #cv2.imshow('image',npimage)
    #cv2.waitKey(round(1000/60))
    
    #t1 = time.time()
    #cv2.waitKey(16)
    #if( (1./60-t1+t0) > 0):
        #time.sleep(1./60.0-(t1-t0))
    #t0 = time.time()
    pygame.display.flip()
    #print("%f \n", clock.get_fps())
t3 = time.time()
print(t3 - t2, "seconds wall time\n")   
pygame.quit()
