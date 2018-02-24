# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:59:27 2018

@author: lukej
"""

import pygame
import pygame.midi

pygame.midi.init() 
input_id = pygame.midi.get_default_input_id() #sets midi id to default
i = pygame.midi.Input( input_id ) #

while True: #This loop only terminates when knob 4 of AKAI MPK mini is rotated, configure for differet MIDI
    if(i.poll() is True): #checks to see if controller is ready to be read
        data=i.read(10)   #reads data from keyboard
        key=data[0][0][1] #pulls key data from data list
        velocity=data[0][0][2] #pulls velocity data from lis
        
        if(velocity!=0): #only reads the data from 
            print(data) 
            print(key,velocity)
            #where we call animation function
        if(key==4): #terminates loop when knob 4 is used 
            break
i.close() #if these lines do not execute, ie keyboard interupt you will need to restart the kernel
pygame.midi.quit()