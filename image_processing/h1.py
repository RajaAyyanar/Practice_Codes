#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:39:54 2018

@author: raja
"""

import numpy as np
from skimage import io,color
from skimage import data
from matplotlib import pyplot as plt

image1=io.imread('cameraman.tif')
image2=data.camera()
plt.imshow(image1)
plt.figure();
io.imshow(image2)
plt.show()

#%%
from skimage import data
from skimage.viewer import ImageViewer

a=ImageViewer(image1)
image = data.coins()
viewer = ImageViewer(image)
viewer.show()

#%%
from skimage.viewer.plugins.lineprofile import LineProfile

viewer = ImageViewer(image)
viewer += LineProfile(viewer)
overlay, data = viewer.show()[0]

#%%
from skimage.viewer.widgets import Slider
from skimage.viewer.widgets.history import SaveButtons

denoise_plugin += Slider('weight', 0.01, 0.5, update_on='release')
denoise_plugin += SaveButtons()
#%%




























