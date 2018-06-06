#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:32:38 2018

@author: raja
"""
import cv2 as cv2
import numpy as np
from skimage import io,color
from skimage import data
from matplotlib import pyplot as plt
#import raja


t= io.imread('plate2.jpg')
#t= io.imread('yellowboard.jpg')
#raja.channelCheck(t)
#c1=raja.crop(t)
plt.imshow(t)
plt.figure()
red=np.copy(t[:,:,0])
green=np.copy(t[:,:,1])
blue=np.copy(t[:,:,2])
plt.hist(blue.ravel(), bins=256, range=[0,256]);plt.show()

red1= red>90
blue1= blue>90
green1= green>90

red[red1]=255
blue[blue1]=255
green[green1]=255

new_pic = np.copy(t)
new_pic[:,:,0]=red
new_pic[:,:,1]=green
new_pic[:,:,2]=blue

plt.imshow(new_pic)













