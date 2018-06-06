#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:07:17 2018

@author: raja
"""


import numpy as np
from skimage import io, color
from skimage import data
from skimage.viewer import ImageViewer
from matplotlib import pyplot as plt

a= data.camera()
io.imshow(a)
 
b= data.coffee()
io.imshow(b)

c=data.coins()
io.imshow(c)

d=io.imread('coloredChips.png')
dd=plt.imshow(d)

r,c,dim=np.shape(d)
new=np.zeros((r,c))

for i in range(0,r):
    for j in range(0,c):
        if ((d[i,j,0]>200) and (d[i,j,1]<48) and (d[i,j,2]<80)):
            new[i,j] = (5*d[i,j,0]+ d[i,j,1] +d[i,j,2])/7
        else:
             new[i,j]= 0
             
plt.figure()
io.imshow(np.uint8(new))












