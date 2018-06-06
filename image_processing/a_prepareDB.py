#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 00:40:50 2018

@author: raja
"""

from skimage import io,color
from skimage import data
import numpy as np
from matplotlib import pyplot as plt
import cv2
from skimage.measure import regionprops
from skimage import measure
from skimage import filters
from scipy.misc import imsave
import skimage


import os

inpath= "/home/raja/mod5_assignment/database/Alphabet_pic1/"
out123="/home/raja/mod5_assignment/database/AlphaNumeric1/"
out=os.listdir(inpath)

for i in out:
    dirPath = inpath+"/%s" %(i)
    fileList = os.listdir(dirPath)
    k=0
    for fileName in fileList:
                
        pic= io.imread(dirPath+'/'+fileName, as_grey=True)
        pic=255*pic
        pic=np.uint8(pic)
        io.imshow(pic)
        val = filters.threshold_otsu(pic)
        ret1,th1 = cv2.threshold(pic,val,255,cv2.THRESH_BINARY_INV)
        io.imshow(th1)
        ret, markers = cv2.connectedComponents(th1)
        properties = measure.regionprops(markers)
        
        for p in properties:
            k=k+1
            #plt.figure()
            #plt.imshow(p.image)
                
            n1=np.uint8(p.image*255)
            new=cv2.resize(n1, (50,40))
            #plt.imshow(new)
            z = out123+'/%s/%s%s.png' %(i,i,str(k))
            imsave(z,new)
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        