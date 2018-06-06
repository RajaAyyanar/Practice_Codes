#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:46:09 2018

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

pic=io.imread('b8.png',as_grey=True)

pic=np.uint8(pic)

val = filters.threshold_otsu(pic)
ret1,th1 = cv2.threshold(pic,val,255,cv2.THRESH_BINARY_INV)
io.imshow(th1)

ret, markers = cv2.connectedComponents(th1)


properties = measure.regionprops(markers)

area1=[prop.area for prop in properties]
perimeter1=[prop.perimeter for prop in properties] 
centroids=[prop.centroid for prop in properties]
boundary= np.array([prop.bbox for prop in properties])
orientation1=np.array([prop.orientation for prop in properties])
bound_area1= np.array([prop.bbox_area for prop in properties])
imag= np.array([prop.image for prop in properties])



centroids=np.array(centroids)
plt.figure(), io.imshow(th1) 
plt.hold(True)
plt.plot(centroids[:,1],centroids[:,0],'r*')


x_min=boundary[:,0]
y_min=boundary[:,1]
small_point=np.array([x_min, y_min]).T
new_centroids= centroids-small_point


k1= imag[0]
k2=imag[1]
"""
image = cv2.resize(pic, (650,300))

k1 = cv2.resize(k1, (43,27))
k2 = cv2.resize(k2, (43,27))
"""
plt.figure()
plt.imshow(k1)
plt.hold(True)
plt.plot(new_centroids[0,1],new_centroids[0,0],'r*')

plt.figure()
plt.imshow(k2)
plt.hold(True)
plt.plot(new_centroids[1,1],new_centroids[1,0],'r*')



























