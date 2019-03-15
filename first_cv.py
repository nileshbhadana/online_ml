#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:28:11 2019

@author: nilesh
"""

import cv2
import numpy as np

np.zeros((500,500,3))

img1=cv2.imread('oak.jpg',flags=cv2.IMREAD_COLOR)[200:600,0:100]
#img2=cv2.imread('oak.jpg',flags=cv2.IMREAD_GRAYSCALE)
#img3=cv2.imread('oak.jpg',flags=cv2.IMREAD_UNCHANGED)
dog=cv2.imread('dog1.jpg')
cat=cv2.imread('cat1.jpg')
final=dog*cat
cv2.imwrite('new_dog.jpg',final)

#rev=1/img
img2=cv2.addWeighted(dog,0.1,cat,0.7,1)
img3=cv2.addWeighted(dog,0.1,cat,0.7,0)
#cv2.imshow('win1',img1)
cv2.imshow('win2',img1)
#cv2.imshow('win3',img3)

cv2.waitKey(0)
#print(img.shape)