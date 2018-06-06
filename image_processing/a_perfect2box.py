#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 12:44:51 2018

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
from scipy.misc import imsave


pic= io.imread('/home/raja/mod5_assignment/Perfect numbers/abcd.png', as_grey=True)
pic=255*pic
pic=np.uint8(pic)
io.imshow(pic)

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

k=0
for p in properties:
    k=k+1
    plt.figure()
    plt.imshow(p.image)
        
    n1=np.uint8(p.image*255)
    new=cv2.resize(n1, (50,40))
    #plt.imshow(new)
    z = '/home/raja/mod5_assignment/single/%s.png' %(str(k))
    imsave(z,new)
    

centroids=np.array(centroids)
plt.figure(), io.imshow(th1) 
plt.hold(True)
plt.plot(centroids[:,1],centroids[:,0],'r*')

n1=np.uint8(imag[2]*255)
new=cv2.resize(n1, (40,50))
plt.imshow(new)











