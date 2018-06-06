#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:37:01 2018

@author: raja
"""

import numpy as np
import scipy
from matplotlib import pyplot as plt
from skimage import io,color

th1=io.imread('circles.png')



x=np.copy(th1)
y=scipy.ndimage.morphology.binary_dilation(x,mask).astype(x.dtype)
y=np.array(y)


mask=np.ones((5,5),dtype=np.int)
mask[0,0]=mask[2,0]=mask[0,2]=mask[2,2]=0

y0=scipy.ndimage.morphology.binary_erosion(x,mask).astype(x.dtype)
y0=np.array(y0)


n=y0  x