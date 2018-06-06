#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:32:39 2018

@author: raja
"""

import numpy as np
from matplotlib import pyplot as plt
from skimage import io,color
from skimage import data
import scipy

pic1= io.imread('number-plates-693.jpg')
io.imshow(pic1)
mask=np.ones((3,3))
mask[1,1]= 8;



plt.hist(pic1[:,:,0].ravel(),256,[100,256]); plt.show()
"""
convolution
after=scipy.ndimage.filters.convolve(pic1,mask)
plt.figure(), io.imshow(after)

"""