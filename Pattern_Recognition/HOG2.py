#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 14:30:06 2018

@author: raja
"""

from skimage import io
from matplotlib import pyplot as plt
import numpy as np

    from skimage import io
    from matplotlib import pyplot as plt
    from scipy import signal
    import numpy as np
    from scipy import ndimage
    
    

pic= io.imread('cman.tif')
r,c=np.shape(pic)

def boxx(box):
    a=np.copy(box)
    b = np.reshape(a, (np.product(a.shape)))
    c=np.zeros(np.shape(b))
    b=b.tolist()
    k=0
    for i in b:
        c[k]=b.count(i)
        k=k+1
    indexx=np.argmax(c)
    return b[indexx]
        
        
boxed=np.zeros((r,c))
k1=0;k2=0

dd=np.zeros((r,c))
k1=8;
for i in range(0,r,8):
    k2=8
    for j in range(0,c,8):
        
        pic2= pic[i:i+k1,j:j+k2]
        dd[i:k1+i,j:k2+j]=boxx(pic2)
        
        
        
io.imshow(dd)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        