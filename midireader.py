# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:59:27 2018

@author: lukej
"""
import random
import pygame
import pygame.midi
import turtle
from turtle import *


clearscreen() #wipes the screen
wn= turtle.Screen() #creates a screen instance
wn.bgcolor('black') #sets the back ground color
hideturtle() #these two lines hide the turtle, which improves performance, and looks better
ht()
x=0
y=0
speed(0) #sets the turtle speed to having no animation, do not  change!!!!!
pygame.midi.init()  #intializes midi
velocity=0  #ensures that the plotting won't begin until a real velocity has been set
input_id = pygame.midi.get_default_input_id() #sets midi id to default
new_key=0           #counter for checking if the key is on stroke down or up 0 for up
cycle_counter=0     #counts the number of cycles

if(input_id == -1):
    print("no device connected!")
else:
    i = pygame.midi.Input( input_id ) #

    while True: #This loop only terminates when knob 4 of AKAI MPK mini is rotated, configure for differet MIDI
        if(i.poll() is True): #checks to see if controller is ready to be read

            data =  i.read(10)           #reads data from keyboard
            control = data[0][0][0]      #control is set to the key type, knobs pads, and keys all have different values
            key = data[0][0][1]          #pulls key data from data list
            if(velocity==0):
                keyOld=key
            if(data[0][0][2] !=0):       #makes sure not to refresh the data on a key up stroke
                velocity = data[0][0][2] #pulls velocity data from list
                new_key=1                #whenever a new key is pressed this is set to 1
            if(key == 4 and control == 176): #terminates loop when knob 4 is used 
                break
            
            
        if(new_key==1):                    #refreshes the location when a new key is pressd
            if(key!=keyOld):
                penup()
                direction=random.randint(0,1)
                if(key>keyOld):
                    if(direction==0):
                        x=(400-x)*1/4+x
                    else:
                        y=(400-y)*1/4+y
                else:
                    if(direction==0):
                        x=(-400-x)*1/4+x
                    else:
                        y=(-400-y)*1/4+y
                goto(x,y)                      #moves the pen to the new location
                pendown()                      #places the pen down at the new location            
            new_key=0                      #resets the "new key" counter
            
        if(velocity != 0):                 #ensures that turtle is not moving when no data is input
            cycle_counter+=1               #counts for the reset later
            if(cycle_counter%5000==0):     #wipes the screen after 5000 lines
                clearscreen()              
                wn.bgcolor('black')
                hideturtle()
                ht()
                cycle_counter=0
                
            red_amount = (key % 100 )/100       #generates the red color
            blue_amount = (key*velocity % 100) /100 #generates the blue color
            green_amount = (velocity %100 ) /100   #generates the green color
            pencolor((red_amount, green_amount, blue_amount)) #sets the color of the pen
            width(100/(key+15)+1.2)             #sets the width of the line
            forward(velocity*1.4+1/(key+1)*20) #sets the amount that the brush moves forward by
            
            if(velocity<42):                   # if the velocity is low set a low angle
                angle=59
            elif(velocity<94):                  #medium velocity is a medium angle
                angle = 88
            else:                               #high velocity high angle
                angle = 117
            left(angle)                         #rotate by angle
            
            
    i.close() #if these lines do not execute, ie keyboard interupt you will need to restart the kernel
pygame.midi.quit()
