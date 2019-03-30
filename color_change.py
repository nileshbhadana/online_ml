#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:11:22 2019

@author: nilesh
"""

import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
    frame=cap.read()[1]
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('color win',frame)
    cv2.imshow('gray win',gray_frame)
    cv2.imshow('RGB win',rgb_frame)
    if cv2.waitKey(10) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()