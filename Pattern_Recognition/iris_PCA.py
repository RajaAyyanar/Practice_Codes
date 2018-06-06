#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 12:41:37 2018

@author: raja
"""


import numpy as np
from sklearn.decomposition import PCA
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1,shuffle=True)

princi= PCA(n_components=4, svd_solver='full')
princi.fit(X)
print(princi.explained_variance_)
print(princi.explained_variance_ratio_)

