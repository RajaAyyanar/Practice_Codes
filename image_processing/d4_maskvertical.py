#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:11:43 2018

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

#mask= np.ones((1,3))/2
#mask[:,1]=0

for i in range(1,254):
    for j in range(1,254):
        y[i,j]=img[i,j]
        if (img[i,j]==0 and img[i+1,j]==0 and img[i-1,j]==0 ):
            subimage=np.array([img[i-1:(i+1)+1, j-1:(j+1)+1]])
            y[i,j]= np.median(np.median(subimage))

io.imshow(np.uint8(y))

img1=io.imread('cameraman.tif')
e6=sum(sum((img1-y)**2)) / np.size(img1)
