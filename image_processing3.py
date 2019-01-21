import numpy as np
import sys
import os
import time
import pygame
import keyboard

#for syncing

import sys


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






# Set up a graphics view and a scene
grview = QGraphicsView()
grview.setViewport(qgl_widget)
scene = QGraphicsScene()
pic = QLabel()

grview = QGraphicsView()
grview.setViewport(qgl_widget)
scene = QGraphicsScene()
scene.addPixmap(QPixmap('pic.jpg'))
grview.setScene(scene)

grview.show()

sys.exit(app.exec_())


getFrame.z = None
#keyboard.read_key()
t2 = time.time()
t0 = time.time()
for i in range(1,600):
    # Get a numpy array to display from the simulation
    getFrame.z = None
    image=getFrame(i)
    #print(np.shape(npimage))
    
    #pygame.surfarray.blit_array(screen,npimage)
    
    #print(t1 - t0, "seconds wall time\n")       
    
    #screen.blit(background, (0, 0)) 
    #cv2.imshow('image',npimage)
    #cv2.waitKey(round(1000/60))
    print(image.shape)
    image = QImage(image, 250,250, image.shape[1] * 3,QImage.Format_RGB888)
    #image = QImage(image, image.shape[1],image.shape[0], image.shape[1] * 3,QImage.Format_RGB888)
    pix = QPixmap(image)
    
    
    pic.setPixmap(pix)
    print(pix)
    print(pic)
    pic.show() # You were missing this.

    #self.scene.addPixmap(pix)    
    #scene.addPixmap(pix)
    #grview.setScene(scene)
    
    #grview.show()
    #print(type(img))
    #img = npimage.astype('uint8')
    #img.blit(100,100)

    t1 = time.time()
    #cv2.waitKey(16)
    #if( (1./60-t1+t0) > 0):
        #time.sleep(1./60.0-(t1-t0))
    #t0 = time.time()
    #pygame.display.flip()
t3 = time.time()
print(t3 - t2, "seconds wall time\n")   
#pygame.quit()
sys.exit(app.exec_())