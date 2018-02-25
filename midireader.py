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

red_amount   =  [0, 0, .878, .686, .498, .251, .282, 0, .373, .275, .69, .69, .678, .529, .529, 0, .118, .392, .482, .255, 0, 0, 0]
green_amount =  [1, 1, 1, .933, 1, .878, .82, .808, .62, .51, .769, .878, .847, .808, .808, .749, .565, .584, .408, .412, 0, 0, 0]
blue_amount  = [1, 1, 1, .933, .831, .816, .8, .82, .627, .706, .871, .902, .902, .922, .98, 1, 1, .929, .933, .882, 1, .804, .545]
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
color_index=0
if(input_id == -1):
    print("no device connected!")
else:
    i = pygame.midi.Input( input_id ) #

    while True: #This loop only terminates when knob 4 of AKAI MPK mini is rotated, configure for differet MIDI
        if(i.poll() is True): #checks to see if controller is ready to be read

            data =  i.read(10)           #reads data from keyboard
            control = data[0][0][0]      #control is set to the key type, knobs pads, and keys all have different values
            key = data[0][0][1]          #pulls key data from data list
            if(data[0][0][2] !=0):       #makes sure not to refresh the data on a key up stroke
                velocity = data[0][0][2] #pulls velocity data from list
                new_key=1                #whenever a new key is pressed this is set to 1
            if(velocity==0):
                keyOld=key
            if(key == 4 and control == 176): #terminates loop when knob 4 is used 
                break
            
            
        if(new_key==1):                    #refreshes the location when a new key is pressd
            color_index+=1                  #changes the color of the line
            if(key!=keyOld):                #makes sure the key isn't being repeated
                penup()                     #prevents the pen from drawing
                if(velocity>74):            #if you press hard it moves right
                    x=(400-x)*1/4+x
                else:                       #if you press lightly moves left
                    x=(-400-x)*1/4+x
                if(key>keyOld):             #if you move up in pitch moves up
                    y=(400-y)*1/5+y
                else:
                    y=(-400-y)*1/5+y        #if you move down in pitch you move down
                goto(x,y)                   #moves the pen to the new location
                pendown()                   #places the pen down at the new location            
            new_key=0                      #resets the "new key" counter
        if(velocity != 0):                 #ensures that turtle is not moving when no data is input
            cycle_counter+=1               #counts for the reset later
            if(cycle_counter==5000):     #wipes the screen after 1000 lines
                clearscreen()              
                wn.bgcolor('black')
                hideturtle()
                ht()
                cycle_counter=0
                speed(0)
                
            red =   red_amount[color_index % len(red_amount)]     #generates the red color
            blue = blue_amount[color_index % len(blue_amount)]#generates the blue color
            green = green_amount[color_index % len(green_amount)]  #generates the green color
            pencolor((red, green, blue)) #sets the color of the pen
            width(100/(key+15)+1.2)             #sets the width of the line
            forward(velocity*1.4+1/(key+1)*20) #sets the amount that the brush moves forward by
            
            if(velocity<42):                   # if the velocity is low set a low angle
                angle=59
            elif(velocity<94):                  #medium velocity is a medium angle
                angle = 88
            else:                               #high velocity high angle
                angle = 117
            left(angle)                         #rotate by angle
            keyOld=key
            
    i.close() #if these lines do not execute, ie keyboard interupt you will need to restart the kernel
pygame.midi.quit()
