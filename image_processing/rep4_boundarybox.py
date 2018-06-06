#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 00:11:00 2018

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

#pic = io.imread('eight.tif');
pic= io.imread('plate2.jpg', as_grey=True)
pic=255*pic
pic=np.uint8(pic)
io.imshow(pic)
#pic= color.rgb2gray(pic1)
#pic= pic*255
val = filters.threshold_otsu(pic)
ret1,th1 = cv2.threshold(pic,val,255,cv2.THRESH_BINARY_INV)
io.imshow(th1)

ret, markers = cv2.connectedComponents(th1)
#ret, markers = cv2.bwlabel(th1)

properties = measure.regionprops(markers)

area1=[prop.area for prop in properties]
perimeter1=[prop.perimeter for prop in properties] 
centroids=[prop.centroid for prop in properties]
boundary= np.array([prop.bbox for prop in properties])
orientation1=np.array([prop.orientation for prop in properties])
bound_area1= np.array([prop.bbox_area for prop in properties])
imag= np.array([prop.image for prop in properties])

k=1
for p in properties:
    a,b,c,d =p.bbox
    if abs((a-b)*(c-d)) > 9000:
        k=k+1
        plt.figure()
        plt.imshow(p.image)


centroids=np.array(centroids)
plt.figure(), io.imshow(th1) 
plt.hold(True)
plt.plot(centroids[:,1],centroids[:,0],'r*')


















