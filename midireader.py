# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:59:27 2018

@author: lukej
"""

import pygame
import pygame.midi
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input( input_id )
while True:
    if(i.poll() is True):
        data=i.read(10)
        key=data[0][0][1]
        velocity=data[0][0][2]
        if(velocity!=0):
            print(data)
            print(key,velocity)
            #where we call animation function
        if(key==4):
            break
i.close()
pygame.midi.quit()