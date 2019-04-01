#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:47:41 2019

@author: nilesh
"""

import cv2
cap=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('/home/nilesh/Desktop/online_ml/face.xml')
cascade2=cv2.CascadeClassifier('/home/nilesh/Desktop/online_ml/eyes.xml')
while cap.isOpened():
    frame=cap.read()[1]
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #face detection
                                     #frame  scale-factor  min neighbour
    faces=cascade.detectMultiScale(gray_frame,1.5,5)
    print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Face Detected',(10,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
    
    # eyes detection
    eyes=cascade2.detectMultiScale(gray_frame,1.5,5)
    print(faces)
    for (x1,y1,w1,h1) in eyes:
        cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
        cv2.putText(frame,'EYES Detected',(10,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
    
    cv2.imshow('win',frame)
    if cv2.waitKey(10) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    