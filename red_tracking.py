
import pygame
import pygame.camera
import numpy
from pygame.locals import *

#ALL COMMENTS ARE RELATED TO iROBOT
#import create
#import time


#r=create.Create(3)
#r.toFullMode()
#sensors=r.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])

last_array=None
diffs=None
shrunken = (320, 240) 
pygame.init()
pygame.camera.init()
size = (1280, 720)

red = (130, 0, 0)
green= (0,205,0)
t = (125, 25, 25)
t2=(20,155,20)
b = (255, 0, 0)
b2=(0,255,0)
t = (65, 25, 25)
d = pygame.display.set_mode(size, 0)
s = pygame.surface.Surface(size)
c = pygame.camera.list_cameras()

cam = pygame.camera.Camera(c[0], size, 'HSV') 
cam.start()
going = True


while going:
   
    s = cam.get_image(s)
    #r.go(20,0)
    #r.printSensors()
     

    #if sensors[create.RIGHT_BUMP]==1:
     #   r.stop()
      #  r.move(-8,5)
       # r.turn(-88,100)
        #time.sleep(.5)
    #elif sensors[create.LEFT_BUMP]==1:
     #   r.stop()
      #  r.move(-8,5)
        # 
        #r.turn(88,100)
       # time.sleep(.5)
    #s2d = pygame.surfarray.array2d(s)
   # s2d = numpy.bitwise_and(s2d, 0xFF)
    #diffs=s2d
    #if last_array != None:
    #    diffs= s2d-last_array
    #last_array=s2d
   # pygame.surfarray.blit_array(s, diffs)

 
   
    m = pygame.mask.from_threshold(s, red, t)
    
    for blob in m.connected_components(10):
        
        coord = blob.centroid()
        pygame.draw.circle(s, b, coord, 50, 5)
        #r.turn(180,100)
       
        #time.sleep(.5)
        break
        

    p = pygame.transform.scale(s, size)
    d.blit(p, (0, 0))
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == QUIT:
            cam.stop()
            going = False
