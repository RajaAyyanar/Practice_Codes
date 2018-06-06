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

k1= np.uint8(k1)
k2= np.uint8(k2)
k1 = cv2.resize(k1, (300,500))
k2 = cv2.resize(k2,(300,500))
properties_k1 = measure.regionprops(k1)
properties_k2 = measure.regionprops(k2)

c1=properties_k1[0].centroid
c2=properties_k2[0].centroid

sym_x1= abs(np.copy(k1)- np.copy(k1[ ::-1,:]))
sym_y1= abs(np.copy(k1)- np.copy(k1[ :, ::-1]))

error_x1 = np.sum(sym_x1)/255
error_y1 = np.sum(sym_y1)/255


sym_x2=abs( np.copy(k2)- np.copy(k2[ ::-1,:]))
sym_y2= abs(np.copy(k2)- np.copy(k2[ :, ::-1]))

error_x2 = np.sum(sym_x2)/255
error_y2 = np.sum(sym_y2)/255

#feature=[centroidx centy vertical horizontal]




















