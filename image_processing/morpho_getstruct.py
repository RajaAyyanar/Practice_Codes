#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:27:23 2018

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

"""https://in.mathworks.com/help/images/ref/strel.html"""


mask=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))


pic= io.imread('text.png')
pic= io.imread('coins.png')

val = filters.threshold_otsu(pic)
ret1,th1 = cv2.threshold(pic,val,255,cv2.THRESH_BINARY)
io.imshow(th1)

pic=np.copy(th1)

plt.imshow(pic)
opening = cv2.morphologyEx(pic, cv2.MORPH_OPEN, mask)
closing = cv2.morphologyEx(pic, cv2.MORPH_CLOSE, mask)
plt.figure(),
plt.imshow(opening)
plt.figure(),
plt.imshow(closing)
