#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:15:05 2018

@author: raja
"""
import scipy

x= np.zeros((7,7),dtype=np.int)
x[2:5,2:6]=1

mask=np.ones((3,3),dtype=np.int)
mask[0,0]=mask[2,0]=mask[0,2]=mask[2,2]=0

y0=scipy.ndimage.morphology.binary_erosion(x,mask).astype(x.dtype)
y0=np.array(y0)

y=scipy.ndimage.morphology.binary_dilation(y0,mask).astype(x.dtype)
y=np.array(y)