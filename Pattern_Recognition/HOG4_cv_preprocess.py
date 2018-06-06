#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 20:19:02 2018

@author: raja
"""

import cv2 as cv2
import raja
import numpy as np

Ori=cv2.imread('/home/raja/Mod 7/test pics/usain_full.jpg')
croped= raja.crop(Ori)
resized_image = cv2.resize(croped, (64,128)) 
cv2.imwrite('/home/raja/Mod 7/test pics/small_usain.jpg',resized_image)


im1=np.copy(pic)
#im=np.copy(im1[:,:,::-1])
im=np.copy(im1[:,:,:])

#plt.subplot(121),plt.imshow(im1)
#plt.subplot(122),plt.imshow(im)
r = cv2.selectROI("Image", im)
imCrop1 = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
#imCrop=imCrop1[:,:,::-1]
imCrop=imCrop1[:,:,:]
