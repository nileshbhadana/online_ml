#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:11:02 2019

@author: nilesh
"""

from sklearn import tree

# weights & shape

# 0----> smooth
# 1 ----> bumpy

features=[[120,0],[50,1],[110,1],[60,0],[100,0],[55,1]]
labels=["apple","orange","apple","orange","apple","orange"]

algo=tree.DecisionTreeClassifier()

#training the algo 
algo.fit(features,labels)

#  prediction
output=algo.predict([[90,1],[65,1]])
print(output)