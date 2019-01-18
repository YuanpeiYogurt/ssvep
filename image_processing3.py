import numpy as np
import sys
import cv2
import os
import time
import pygame
import keyboard

import pyglet
from pyglet import clock
from PIL import Image


WIDTH = 250
HEIGHT = 250
FPS_LIMIT = 60
UPDATE_INTERVAL = 1 / 30
VSYNC = True

window = pyglet.window.Window(WIDTH, HEIGHT)
window.set_vsync(VSYNC)


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

#pygame.init()

#window = (stimSize,stimSize)
#screen = pygame.display.set_mode(window)
#background = pygame.Surface(window)

    
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
t2 = time.time()
t0 = time.time()
#clock = pygame.time.Clock()
for i in range(1,600):
    #clock.tick()
    #print(clock.get_fps())
    # Get a numpy array to display from the simulation
    getFrame.z = None
    npimage=getFrame(i)
    #print(np.shape(npimage))
    
    #pygame.surfarray.blit_array(screen,npimage)
    
    #print(t1 - t0, "seconds wall time\n")       
    
    #screen.blit(background, (0, 0)) 
    #cv2.imshow('image',npimage)
    #cv2.waitKey(round(1000/60))
    
    #img = pyglet.extlibs.png.from_array(npimg)
    img = png.fromarray(npimage, 'RGB')
    #print(type(img))
    #img = npimage.astype('uint8')
    #img.blit(100,100)
    
    sprite = pyglet.sprite.Sprite(img=npimage)
    
    @window.event
    def on_draw():
        window.clear()
        sprite.draw()    
    
    
    
    t1 = time.time()
    #cv2.waitKey(16)
    #if( (1./60-t1+t0) > 0):
        #time.sleep(1./60.0-(t1-t0))
    #t0 = time.time()
    #pygame.display.flip()
t3 = time.time()
print(t3 - t2, "seconds wall time\n")   
#pygame.quit()
pyglet.app.exit()