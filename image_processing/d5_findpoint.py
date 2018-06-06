#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:03:09 2018

@author: raja
"""

import numpy as np
from skimage import io,color
from skimage import data
from matplotlib import pyplot as plt


pic= io.imread('coloredChips.png')
pic2= color.rgb2grey(pic)
#pic2 = 0.21*pic[:,:,0] + 0.72*pic[:,:,1] + 0.07*pic[:,:,2] 
#io.imshow(pic2)
#pic2= np.uint8(pic2)
pic2[100,100]= 1
io.imshow(pic2)


mask= np.ones((3,3))
mask[1,1]=-8

a,b = np.shape(pic2)
y=np.zeros(np.shape(pic2))
for i in range(1,a-1):
    for j in range(1,b-1):
        subimage=pic2[i-1:(i+1)+1 , j-1:(j+1)+1]
        y[i,j]= sum(sum(subimage * mask))

plt.figure()
io.imshow(y)

new_y= np.zeros((np.shape(y)))

new_y[ y< -2.2] =255
plt.figure()
io.imshow(new_y)


















