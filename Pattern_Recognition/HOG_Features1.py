#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:29:07 2018

@author: raja
"""
import cv2
image = cv2.imread('/home/raja/Mod 7/test pics/1.jpg',0)
#image=image[0:48,0:64]
winSize = (64,64)
blockSize = (16,16)
blockStride = (8,8)
cellSize = (8,8)
nbins = 9
derivAperture = 1
winSigma = 4.
histogramNormType = 0
L2HysThreshold = 2.0000000000000001e-01
gammaCorrection = 0
nlevels = 64
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,
                        histogramNormType,L2HysThreshold,gammaCorrection,nlevels)
#compute(img[, winStride[, padding[, locations]]]) -> descriptors
winStride = (8,8)
padding = (8,8)
locations = ((120,120),)
hist = hog.compute(image,winStride,padding)