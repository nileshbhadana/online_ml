#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:09:09 2019

@author: nilesh
"""

import cv2,numpy as np

cap=cv2.VideoCapture(0)
counter=0
while cap.isOpened():
    #status,frame=cap.read()
    frame=cap.read()[1]
    #img=cv2.imread()
    #final=frame+img
    #print(frame)
    cv2.line(frame,(0,0),(100,100),(254,254,254),10)
    print(np.shape(frame))    #camera resolution
    
    #counter=counter+1
    #cv2.imwrite('/home/nilesh/Desktop/online_ml/'+str(counter)+'.jpg',frame)
    #print(status)
    cv2.imshow('live',frame[0:250,0:500])
    #cv2.waitKey(10)
    
    #creating handler
    if cv2.waitKey(10) & 0xff == ord('q'): #ord===ascii values
        break
    
    
cap.release()    #closing camera
cv2.destroyAllWindows()    #destroying live window
print(cap.isOpened())    
#print(cap.isOpened())