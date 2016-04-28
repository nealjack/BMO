#!/usr/bin/python
#
# Sprite Sheet Loader - hammythepig
#
# Edited by Peter Kennedy
#
# License - Attribution - hammythepig
    #http://stackoverflow.com/questions/10560446/how-do-you-select-a-sprite-image-from-a-sprite-sheet-in-python
#
# Version = '2.0'

import pygame,sys
from pygame.locals import *
import sys,os

def sprite_sheet(size,file,pos=(0,0)):

    #Initial Values
    len_sprt_x,len_sprt_y = size #sprite size
    sprt_rect_x,sprt_rect_y = pos #where to find first sprite on sheet
    try:
        sheet = pygame.image.load(file).convert_alpha() #Load the sheet
    except:
        print(os.path.exists(file))
        sys.exit()
    sheet_rect = sheet.get_rect()
    sprites = []
    print (sheet_rect.height, sheet_rect.width)
    while sprt_rect_y<sheet_rect.height:#rows
        print ("row")
        sprt_rect_x = 0
        while sprt_rect_x<sheet_rect.width:#columns
            print ("column")
            sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y)) #find sprite you want
            sprite = sheet.subsurface(sheet.get_clip()) #grab the sprite you want
            sprites.append(sprite)
            sprt_rect_x += len_sprt_x

        sprt_rect_y += len_sprt_y
    print (sprites)
    return sprites

#VERSION HISTORY

    #1.1 - turned code into useable function

    #2.0 - fully functional sprite sheet loader
