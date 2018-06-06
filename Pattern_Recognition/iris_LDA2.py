#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 12:23:55 2018

@author: raja
"""

# Import needed packages
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import datasets

# Bring in dataset and get features
iris = datasets.load_iris()
allFeatures = iris['data']
y = iris['target']
x = allFeatures[:, 0]
x = x.reshape(150, 1)
y = y.reshape(150, 1)

# Plot data
plt.clf()
plt.scatter(x,y)
plt.show()

# Linear discrimant analysis
clf = LinearDiscriminantAnalysis()
clf.fit(x, y)
print(clf.predict([1]))