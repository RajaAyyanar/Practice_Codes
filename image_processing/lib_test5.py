#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 23:00:08 2018

@author: raja
"""
import cv2 as cv2
from skimage import io,color 
# Read image
im = io.imread("plate2.jpg")

# Select ROI
#r = cv2.selectROI(im)
r = cv2.selectROI("Image", im) 
# Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# Display cropped image
cv2.imshow("Image", imCrop)
cv2.waitKey(0)