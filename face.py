#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 18:08:02 2021

@author: saikrishnapaila
"""

import cv2

#loaded with pre-trained data on face frontals from opencv
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#for front cam
webcam=cv2.VideoCapture(0)
#infinte loop untill we press q button key
while True:
    #read current running frame
    successful_frame_read, frame= webcam.read()
    
    #must convert to grayscale for face coordinates
    grayscaled_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    # collect coordinates from grayscale
    face_coordinates= trained_face_data.detectMultiScale(grayscaled_img)
    
    #loop is for multiple face on frame
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),2)
        
    #it shows webcam of your laptop or computer
    cv2.imshow('krish',frame)
    
    key=cv2.waitKey(1)
    
    #if u press Q or q button then the loop will break ...81==Q and 113==q ascii values
    if key==81 or key==113:
        break
webcam.release()

print('code executed')