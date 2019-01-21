import numpy as np
import time
import pygame

rcycles = 14
tcycles = 12
stimSize = 250
xylim = 2 * np.pi * rcycles
freq = 10
# color variable
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
    # Generate next frame of simulation as numpy array
    if getFrame.z is None: 
        # for the mesh grid
        x2, y2 = np.meshgrid(np.linspace(-xylim,xylim,stimSize), np.linspace(-xylim,xylim,stimSize))
        # Get the value of the pixel function
        
        getFrame.z = circularcheckerboard(x2, y2,n)
    return getFrame.z


def sin2d(x,y):
    return np.sin(x) + np.cos(y)


def circularcheckerboard(x1,y1,n):
    # ased on matlab code
    at = np.arctan2(x1,y1)
    phiAngle=(np.pi/2)+(np.pi/2)*np.sin((2*np.pi*n*(freq/(4*60)))-(np.pi/2)) 
    
    checks = np.sign(np.cos(np.pi*np.sqrt(x1**2 + y1**2)/D+phiAngle*(L/D))*np.cos(at*tcycles))

    circle = ((x1**2 + y1**2) <= xylim**2)*1
    checks = checks * circle
    return checks


getFrame.z = None
clock = pygame.time.Clock()
t2 = time.time()
for i in range(1, 600):
    # Get a numpy array to display from the simulation
    getFrame.z = None
    npimage = getFrame(i)
    pygame.surfarray.blit_array(screen, npimage)
    pygame.display.flip()
t3 = time.time()
print(t3 - t2, "seconds wall time\n")   
pygame.quit()
