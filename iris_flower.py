#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:51:46 2019

@author: nilesh
"""
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
# targets -----> labels
# data ----> features
#  feature_name , target_names

iris_data=load_iris().data
iris_targets=load_iris().target

algo=tree.DecisionTreeClassifier()

train_data,test_data,train_label,test_label=train_test_split(iris_data,iris_targets,test_size=0.3)

print(len(train_data),len(test_data),len(train_label),len(test_label))

train=algo.fit(train_data,train_label)

# prediction
predicted_output=algo.predict(test_data)

print(predicted_output)
print(test_label)

score=accuracy_score(predicted_output,test_label)
print(score)