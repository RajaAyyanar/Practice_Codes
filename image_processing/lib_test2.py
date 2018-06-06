#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:31:36 2018

@author: raja
"""

import numpy as np
from skimage import io, color
from skimage import data
from skimage.viewer import ImageViewer
from matplotlib import pyplot as plt

"""
%matplotlib inline
%matplotlib qt
"""

a=data.astronaut()
b=data.binary_blobs()
c=data.camera()
plt.subplot(1,3,1),io.imshow(a)
plt.subplot(1,3,2),io.imshow(b)
plt.subplot(1,3,3),io.imshow(c)

plt.figure(),

plt.subplot(1,3,1),io.imshow(c)
plt.subplot(1,3,2),io.imshow(a)
plt.subplot(1,3,3),io.imshow(b)


pic1= io.imread('number-plates-693.jpg')
plt.hist(pic1[:,:,0].ravel(),256,[0,256]); plt.show()