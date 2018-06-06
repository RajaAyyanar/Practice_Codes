#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:45:39 2018

@author: raja
sudo apt-get install texlive-full texmaker


"""



import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt

def channelCheck(pic):
    
    s=np.array([np.shape(pic)])
    channel=s.shape[1]

    if channel !=3:
        print('Uploaded pic is not a 3 channel colored image')
        raise ValueError("Not colored image. Please check your input image");
        
    print('Good to go- 3 channel')
    
def crop(pic):    
    im1=np.copy(pic)
    im=np.copy(im1[:,:,::-1])
    #plt.subplot(121),plt.imshow(im1)
    #plt.subplot(122),plt.imshow(im)
    r = cv2.selectROI("Image", im)
    imCrop1 = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    imCrop=imCrop1[:,:,::-1]
    return imCrop






















