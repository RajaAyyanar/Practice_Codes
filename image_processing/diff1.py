#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:40:44 2018

@author: raja
"""

from skimage import io, color
import numpy as np
from matplotlib import pyplot as plt


img = io.imread('cameraman.tif')
img[:,200]=0
y=np.zeros(np.shape(img))
plt.imshow(img)
#mask= np.ones((3,3))/9

mask= np.ones((3,3))
mask[0,0]=mask[2,0]=mask[0,2]=mask[2,2]=0
mask[1,1]=-4
for i in range(1,254):
    for j in range(1,254):
        subimage=img[i-1:(i+1)+1 , j-1:(j+1)+1]
        y[i,j]= sum(sum(subimage * mask))

io.imshow(np.uint8(y))


img1=io.imread('cameraman.tif')
e8=sum(sum((img1-y)**2)) / np.size(img1)


