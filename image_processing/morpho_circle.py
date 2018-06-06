#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:05:19 2018

@author: raja
"""


from skimage import io,color
from skimage import data
import numpy as np
from matplotlib import pyplot as plt
import cv2
from skimage.measure import regionprops
from skimage import measure
from skimage import filters
import matplotlib
import scipy

pic= io.imread('circles.png')
#pic=io.imread('text.png')
io.imshow(pic)

val = filters.threshold_otsu(pic)
ret1,th1 = cv2.threshold(pic,val,255,cv2.THRESH_BINARY)
io.imshow(th1)

ret, markers = cv2.connectedComponents(th1)



mask=np.ones((21,21),dtype=np.int)
mask[0,0]=mask[20,0]=mask[0,20]=mask[20,20]=0

x=np.copy(th1)
y0=scipy.ndimage.morphology.binary_erosion(x,mask).astype(x.dtype)
y0=np.array(y0)
y=np.copy(y0)

"""
y=scipy.ndimage.morphology.binary_dilation(y0,mask).astype(x.dtype)
y=np.array(y)
"""

ret, markers = cv2.connectedComponents(y)  
io.imshow(y)





























