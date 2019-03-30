#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:40:28 2019

@author: nilesh
"""

import cv2

cap=cv2.VideoCapture(0)

while cap.isOpened():
    frame=cap.read()[1]
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img=cv2.inRange(frame,(0,30,0),(20,255,20))
    img2=cv2.inRange(frame,(0,0,20),(20,20,255))
    
    final=img+img2
    cv2.imshow('color',final)
    cv2.imshow('green',img)
    cv2.imshow('red',img2)
    cv2.imshow('original',frame)
    if cv2.waitKey(10) & 0xff==ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()