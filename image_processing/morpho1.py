#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:57:43 2018

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

[prop.area for prop in properties]
[prop.perimeter for prop in properties] 
k=[prop.centroid for prop in properties]
boundary= np.array([prop.bbox for prop in properties])


k=np.array(k)
plt.figure(), io.imshow(th1) 
plt.hold(True)
plt.plot(k[:,1],k[:,0],'r*')


plt.rectangle(1,1,2,3)



















