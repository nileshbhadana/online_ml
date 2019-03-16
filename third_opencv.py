#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:14:43 2019

@author: nilesh
"""

import cv2,numpy as np
img=np.zeros((600,600,3))
cv2.line(img,(50,50),(300,50),(25,25,0),2)
cv2.rectangle(img,(100,100),(400,400),(50,0,0),-1)


cv2.line(img,(50,50),(50,100),(50,0,0),2)
cv2.line(img,(50,100),(100,100),(0,50,0),2)
cv2.line(img,(100,100),(100,50),(0,0,50),2)
cv2.line(img,(100,50),(50,50),(50,0,0),2)

cv2.circle(img,(75,75),50,(50,50,0),1)
cv2.line(img,(10,10),(10,200),(75,0,78),1)
cv2.line(img,(10,200),(200,200),(75,0,78),1)
cv2.line(img,(200,200),(10,10),(75,0,78),1)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'ADHOC',(50,350),font,3,(51,54,0),3)

cv2.imshow('wind',img)
cv2.waitKey(0)