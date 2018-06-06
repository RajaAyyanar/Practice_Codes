#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:36:12 2018

@author: raja
"""

import numpy as np
from skimage import io,color
from skimage import data
from skimage.viewer import ImageViewer
from matplotlib import pyplot as plt


img = data.astronaut()
gr= color.rgb2gray(img)
g2= color.rgb2grey(img)

io.imshow(gr)
plt.figure()
io.imshow(g2)

#reverse image or mirror image
g3=g2[:,::-1]
plt.figure()
io.imshow(g3)