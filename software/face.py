import pygame, sys, os
from pygame.locals import *
from sprite_sheet import *
from animate import *
from pyscope import *
import xbox_read

#initialize pygame
pygame.init()
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 20

#initialize window
size = (640, 480)
try:
    scope = pyscope()
    surface = scope.screen
except:
    surface = pygame.display.set_mode(size)
size = (pygame.display.Info().current_w,pygame.display.Info().current_h)
pygame.mouse.set_visible(False)
##surface.set_caption('BMO')

#initialize object/colors
backColor = pygame.Color(198,227,193)

#initialize sound mixer
pygame.mixer.init()
frequency,form,channels = pygame.mixer.get_init()
print('frequency: ',frequency,'format: ',form,'channels: ',channels)
pygame.mixer.stop()

#initialize sprites
mouthSize = (150,75)
mouthPos = (size[0]/2-mouthSize[0]/2,size[1]-(150+mouthSize[1]/2))
mouths = sprite_sheet(mouthSize,'../assets/images/mouthSheet.png')
eyeSize = (50,50)
eyePosLeft = (120-eyeSize[0]/2,120-eyeSize[1]/2)
eyePosRight = (size[0]-120-eyeSize[0]/2,eyePosLeft[1])
eyes = sprite_sheet(eyeSize,'../assets/images/eyeSheet.png')

#initialize sounds
ani = animate(pygame)

run = True
while run:
    surface.fill(backColor)
    surface.blit(mouths[ani.update()],mouthPos)
    eye = eyes[0]
    surface.blit(eye,eyePosLeft)
    surface.blit(pygame.transform.flip(eye,True,False),eyePosRight)
    for event in xbox_read.event_stream(deadzone = 12000):
        if event.key == 'guide' and event.value == 1:
           run = False
           break
        else:
            break
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False #stops loop from next iteration
            break
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
                break
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
pygame.quit()#quits window
    
