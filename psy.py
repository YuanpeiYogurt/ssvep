from psychopy import visual, core
import numpy as np
import time
import keyboard

rcycles = 14
tcycles = 12
stimSize = 128
xylim = 2 * np.pi * rcycles
freq1 = 7.5
freq2 = 10
freq3 = 12
freq4 = 13
# color variable
white = 180
grey = 100
black = 0
D=10
L=18
pos1 = (256, 100)
pos2 = (-256, 100)
pos3 = (256, -100)
pos4 = (-256, -100)

playtime = 6
pausetime = 4

#def getFrame(n,freq):
#    #Generate next frame of simulation as numpy array
#    if getFrame.z is None: 
#        #for the meshgrid
#        x2, y2 = np.meshgrid(np.linspace(-xylim,xylim,stimSize), np.linspace(-xylim,xylim,stimSize))
#        #Get the value of the pixel function
#        getFrame.z = circularCheckerBoard(x2, y2,n,freq)      
#    return getFrame.z

def getFrame(n, freq):
    x1, y1 = np.meshgrid(np.linspace(-xylim, xylim, stimSize), np.linspace(-xylim, xylim, stimSize))
    at = np.arctan2(x1, y1)
    phiAngle = (np.pi/2)+(np.pi/2)*np.sin((2*np.pi*n*(freq/(2*60)))-(np.pi/2))
    checks = np.sign(np.cos((np.pi*np.sqrt(x1**2 + y1**2)/D)+phiAngle*(L/D))*np.cos(at*tcycles))
    circle1 = ((x1**2 + y1**2) <= xylim**2)*1
    circle2 = ((x1**2 + y1**2) >= 30)*1
    checks = checks * circle1 * circle2
    return checks


def sin2d(x, y):
    return np.sin(x) + np.cos(y)


def circularCheckerBoard(x1,y1,n,freq):
    # based on matlab code
    at = np.arctan2(x1, y1)
    phiAngle = (np.pi/2)+(np.pi/2)*np.sin((2*np.pi*n*(freq/(2*60)))-(np.pi/2))
    checks = np.sign(np.cos(np.pi*np.sqrt(x1**2 + y1**2)/D+phiAngle*(L/D))*np.cos(at*tcycles))
    circle1 = ((x1**2 + y1**2) <= xylim**2)*1
    circle2 = ((x1**2 + y1**2) >= 10)*1
    checks = checks * circle1 * circle2
    return checks


if __name__ == '__main__':

    # setup stimulus
    win = visual.Window([1024, 512])
    keyboard.read_key()
    t0 = time.time()
    for j in range(1, 4):
        clock1 = core.Clock()

        for i in range(1, 400):
            npimage1 = getFrame(i, freq1)
            checkerboard1 = visual.GratingStim(win, tex=npimage1, size=(128, 128), units='pix')
            checkerboard1.pos = pos1
            npimage2 = getFrame(i, freq2)
            checkerboard2 = visual.GratingStim(win, tex=npimage2, size=(256, 256), units='pix')
            checkerboard2.pos = pos2
            npimage3 = getFrame(i, freq3)
            checkerboard3 = visual.GratingStim(win, tex=npimage3, size=(256, 256), units='pix')
            checkerboard3.pos = pos3
            npimage4 = getFrame(i, freq4)
            checkerboard4 = visual.GratingStim(win, tex=npimage4, size=(256, 256), units='pix')
            checkerboard4.pos = pos4
            checkerboard1.draw()
            checkerboard2.draw()
            checkerboard3.draw()
            checkerboard4.draw()
            win.flip()
            if clock1.getTime() > playtime:
                break
        win.flip()
        time.sleep(pausetime)
    t1 = time.time()    
    print(t1-t0)

