#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 20:59:34 2018

@author: raja
"""

import cv2 as cv2
import numpy as np

# Python gradient calculation 
 
# Read image
img = cv2.imread('/home/raja/Mod 7/test pics/small_usain.jpg')
img = np.float32(img) / 255.0
 
# Calculate gradient 
gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)

# Python Calculate gradient magnitude and direction ( in degrees ) 
mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
