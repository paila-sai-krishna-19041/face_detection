#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 18:08:02 2021

@author: saikrishnapaila
"""
#face Detection on img
import cv2

#loaded with pre-trained data on face frontals from opencv
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img=cv2.imread('RDJ2.png') #you can replace RDJ2 with some other piture which is present in your laptop or computer
#infinte loop untill we press q button key
while True:
   
    
    grayscaled_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    # collect coordinates from grayscale
    face_coordinates= trained_face_data.detectMultiScale(grayscaled_img)
    
    #loop is for multiple face on frame
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)
        
    #it shows webcam of your laptop or computer
    cv2.imshow('krish',img)
    
    key=cv2.waitKey()
    
    #if u press Q or q button then the loop will break ...81==Q and 113==q ascii values
    if key==81 or key==113:
        break

print('code executed')