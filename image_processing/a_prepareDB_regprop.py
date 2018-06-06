#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 00:16:37 2018

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

inpath= "/home/raja/mod5_assignment/Datasets/English_fnt/Fnt/"
outpath="/home/raja/mod5_assignment/Datasets/English_fnt_regionprobs/"
out=os.listdir(inpath)

status=0
for i in out:
    status+=1
    print(status)
    dirPath = inpath+"/%s" %(i)
    fileList = os.listdir(dirPath)
    k=0
    out111=outpath+"%s" %(i)
    os.makedirs(out111,exist_ok=True)
    
    for fileName in fileList:
                
        pic= io.imread(dirPath+'/'+fileName, as_grey=True)
        #pic=255*pic
        pic=np.uint8(pic)
        #io.imshow(pic)
        val = filters.threshold_otsu(pic)
        ret1,th1 = cv2.threshold(pic,val,255,cv2.THRESH_BINARY_INV)
        #io.imshow(th1)
        ret, markers = cv2.connectedComponents(th1)
        properties = measure.regionprops(markers)
        
        for p in properties:
            k=k+1
            #plt.figure()
            #plt.imshow(p.image)
                
            n1=np.uint8(p.image*255)
            new=cv2.resize(n1, (50,50))
            #plt.imshow(new)
            
            z = out111+'/%s.png' %(fileName)
            imsave(z,new)





















