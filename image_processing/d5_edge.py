#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:06:28 2018

@author: raja
"""


import numpy as np
from skimage import io,color
from skimage import data
from matplotlib import pyplot as plt

p= data.camera()
io.imshow(p)

def edgee(p,mask):
        
    a,b = np.shape(pic2)
    y=np.zeros(np.shape(pic2))
    for i in range(1,a-1):
        for j in range(1,b-1):
            subimage=pic2[i-1:(i+1)+1 , j-1:(j+1)+1]
            y[i,j]= sum(sum(subimage * mask))
    
    return y


sobel_mask= np.zeros((3,3))
sobel_mask=[]



plt.figure()
subplot(2,2,1), plt.imshow(y1)