import pygame,sys
import random,math
from pygame.locals import *
import xbox_read

class animate:
    count = 0
    def __init__(self,game):
        self.iamBMOSound = game.mixer.Sound('../assets/sounds/iamBMO.ogg')
        self.wellHelloSound = game.mixer.Sound('../assets/sounds/wellHello.ogg')
        self.teachSound = game.mixer.Sound('../assets/sounds/teachMe.ogg')
        self.face = 1
        self.done = True
        self.timer = 0
        self.count = 0
        self.selection = -1
        
    def update(self):
        if self.done:
            if self.timer <= 100:
                self.timer+=1
            else:
                self.timer=0
                self.count=0
                self.selection = self.select()
        else:
            self.count += 1
        self.face, self.done = self.play(self.selection)
        return self.face

    def select(self):
        select = math.floor(random.random()*3)
        return select
##        for event in xbox_read.event_stream(deadzone=12000):
##            if event.key == 'A':
##                if event.value == 1:
##                    return 0
##            elif event.key == 'B':
##                if event.value == 1:
##                    return 1
##            elif event.key == 'X':
##                if event.value == 1:
##                    return 2
##            elif event.key == 'Y':
##                if event.value == 1:
##                    return 3
##            else:
##                return -1

    def play(self,selection):
        if selection == 0:
            return self.hello(self.count)
        elif selection == 1:
            return self.nameBMO(self.count)
        elif selection == 2:
            return self.teach(self.count)
##        elif selection == 3:
##
        else:
            self.selection = -1
            return (1,True)
        
    def nameBMO(self,count):
        if count == 0:
            self.iamBMOSound.play()
            return (1,False)
        elif count >= 0 and count < 6:
            return (1,False)
        elif (count >= 6 and count < 9) or (count >= 12 and count < 16):
            return (5,False)
        elif (count >= 9 and count < 12) or (count >=19 and count < 22):
            return (3,False)
        elif count>=16 and count<19:
            return (4,False)
        else:
            return (1,True)
        
    def hello(self,count):
        if count == 0:
            self.wellHelloSound.play()
            return (1,False)
        elif (count >= 0 and count < 4) or (count >=12 and count < 16):
            return (1,False)
        elif count >= 4 and count < 8:
            return (4,False)
        elif (count >= 8 and count < 12) or (count >= 16 and count < 17) or (count >= 18 and count < 22):
            return (5,False)
        elif count >= 17 and count < 18:
            return (4,False)
        elif count >=22 and count < 26:
            return (6,False)
        else:
            return (1,True)
        
    def teach(self,count):
        if count == 0:
            self.teachSound.play()
            return (1,False)
        elif (count >= 0 and count < 6) or (count >= 13 and count < 15):
            return(1,False)
        elif (count >= 6 and count < 7) or (count >= 9 and count < 13) or (count >= 23 and count < 25):
            return (3,False)
        elif (count >= 7 and count < 9) or (count >= 28 and count < 30):
            return (4,False)
        elif (count >= 15 and count < 16) or (count >= 21 and count < 23)or (count >= 30 and count < 35):
            return (6,False)
        elif (count >= 20 and count < 21) or (count >= 16 and count < 20) or (count >= 25 and count < 28) or (count >= 35 and count <38):
            return (5,False)
        else:
            return (1,True)
