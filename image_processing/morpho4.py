#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:55:20 2018

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

#pic = io.imread('eight.tif');
pic= io.imread('rice.png')#, as_grey=True)
#pic=io.imread('text.png')

#pic=255*pic
#pic=np.uint8(pic)
io.imshow(pic)
#pic= color.rgb2gray(pic1)
#pic= pic*255
val = filters.threshold_otsu(pic)
ret1,th1 = cv2.threshold(pic,val,255,cv2.THRESH_BINARY)
io.imshow(th1)

ret, markers = cv2.connectedComponents(th1)
#ret, markers = cv2.bwlabel(th1)



mask=np.ones((3,3),dtype=np.int)
mask[0,0]=mask[2,0]=mask[0,2]=mask[2,2]=0

x=np.copy(th1)
y0=scipy.ndimage.morphology.binary_erosion(x,mask).astype(x.dtype)
y0=np.array(y0)

y=scipy.ndimage.morphology.binary_dilation(y0,mask).astype(x.dtype)
y=np.array(y)


ret, markers = cv2.connectedComponents(y)   #95  
io.imshow(y)

properties = measure.regionprops(markers)
[prop.area for prop in properties]
box=[prop.bbox for prop in properties]
box=np.array(box)


plt.imshow('rice.png')
plt.hold(True)















