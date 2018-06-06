#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:02:30 2018

@author: raja
"""

import skimage
import numpy as np
import cv2
from skimage import io,color

m1= io.imread

a=skimage.measure.compare_ssim(m1,m1, win_size=None, gradient=False, 
                               data_range=None, multichannel=False, 
                               gaussian_weights=False, full=False)















