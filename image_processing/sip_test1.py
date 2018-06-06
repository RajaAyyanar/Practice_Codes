#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:13:14 2018

@author: raja
"""

from skimage import io, color
import numpy as np


img = io.imread('baboon.png')
dimensions = color.guess_spatial_dimensions(img)
print (dimensions)

io.imshow(img)
y=color.rgb2gray(img)
y2=1-y
io.imshow(y2)

y3=1-img
io.imshow(y3)
