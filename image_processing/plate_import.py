#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:23:33 2018

@author: raja
"""

import numpy as np
from matplotlib import pyplot as plt
from skimage import io,color
from skimage import data


pic1= io.imread('number-plates-693.jpg')
io.imshow(pic1)

plt.figure()
pic2= io.imread('plate2.jpg')
io.imshow(pic2)

plt.figure()
pic3= io.imread('yellowboard.jpg')
io.imshow(pic3)


e=np.copy(pic1)

ind= e > 150
e = e* ind.astype(int)

io.imshow(np.uint8(e))



























