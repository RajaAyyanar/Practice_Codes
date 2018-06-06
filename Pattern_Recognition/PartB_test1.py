#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:02:44 2018

@author: raja
"""
import cv2
hog = cv2.HOGDescriptor()

img = cv2.imread('/home/raja/Mod 7/test pics/1.jpg')
#im = cv2.imread(sample)
h = hog.compute(img)