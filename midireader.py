# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:59:27 2018

@author: lukej
"""

import pygame
import pygame.midi
#import turtle
from turtle import *



hideturtle()
ht()
speed(0)
pygame.midi.init() 
velocity=0
input_id = pygame.midi.get_default_input_id() #sets midi id to default
draw_counter=0
new_velocity=0
if(input_id == -1):
    print("no device connected!")
else:
    i = pygame.midi.Input( input_id ) #

    while True: #This loop only terminates when knob 4 of AKAI MPK mini is rotated, configure for differet MIDI
        if(i.poll() is True): #checks to see if controller is ready to be read
            data =  i.read(10)   #reads data from keyboard
            key = data[0][0][1] #pulls key data from data list
            if(data[0][0][2] !=0):
                velocity = data[0][0][2] #pulls velocity data from list
                new_velocity=1
            #if(velocity != 0): #only reads the data from 
            print(data) 
            print(key,velocity)
            #animation(key,velocity)
                #where we call animation function
            if(key == 4): #terminates loop when knob 4 is used 
                break
        if(new_velocity==1):
            penup()
            goto((key*velocity^2) % 100 - 100,(key*velocity) % 100 - 100)
            pendown()
            new_velocity=0
        if(velocity != 0):    
            red_amount = (key % 100 )/100
            blue_amount = (key*velocity % 100) /100
            green_amount = (velocity %100 ) /100
            pencolor((red_amount, green_amount, blue_amount))
            width(key/100+1)
            forward(velocity)
            left(59)
    i.close() #if these lines do not execute, ie keyboard interupt you will need to restart the kernel
pygame.midi.quit()
