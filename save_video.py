#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:31:13 2019

@author: nilesh
"""

import cv2
cap=cv2.VideoCapture(0)

cv_decoder=cv2.VideoWriter_fourcc(*'XVID')   # decoder name

                      # video file name  decoder   fps   resolution
v_out=cv2.VideoWriter('/home/nilesh/Desktop/online_ml/first_video.avi',cv_decoder,10,(640,480))
while cap.isOpened():
    frame=cap.read()[1]
    cv2.imshow('save win',frame)
    
    #starting to write in video
    v_out.write(frame)
    
    if cv2.waitKey(10) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()