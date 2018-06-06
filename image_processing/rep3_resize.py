#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:49:42 2018

@author: raja
"""

import cv2 as cv2
import numpy as np
from skimage import io,color
from skimage import data
from matplotlib import pyplot as plt
from skimage.measure import regionprops
from skimage import measure
from skimage import filters
from skimage import transform
import scipy


original = io.imread('plate2.jpg')
out = cv2.resize(original, (650,300))
image=np.copy(original)
#small = scipy.misc.imresize(image, 0.5)
small = scipy.misc.imresize(image, (300,500))

