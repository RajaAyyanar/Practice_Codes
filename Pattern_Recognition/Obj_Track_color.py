#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:20:33 2018

@author: raja
"""

import numpy as np
from skimage import io,color
import cv2
from matplotlib import pyplot as plt

pic= io.imread('/home/raja/Mod 7/Tiger2/img/0047.jpg')


(r,c,d) = np.shape(pic)
trak=np.zeros((r,c))

for i in range(0,r):
    for j in range(0,c):
        if pic[i,j,0]>150 and pic[i,j,0]<210 and pic[i,j,1]>40 and pic[i,j,1]<80 and pic[i,j,2]>10 and pic[i,j,2]<40 :
            trak[i,j]=255
        
yy=pic[83:83+78,59:59+68,:]
yy=pic[60:60+78,32:32+68,:]


plt.figure()
plt.subplot(3,2,5);plt.imshow(pic)
plt.title('Original Pic')
plt.subplot(3,2,6);plt.imshow(trak)
plt.title('Predicted/ Tracked data')
plt.hold(True)
