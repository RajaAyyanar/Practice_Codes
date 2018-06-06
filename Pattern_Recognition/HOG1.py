#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:02:56 2018

@author: raja
"""

    from skimage import io
    from matplotlib import pyplot as plt
    from scipy import signal
    import numpy as np
    from scipy import ndimage
    
    
from skimage import io
from matplotlib import pyplot as plt
from scipy import signal
import numpy as np
from scipy import ndimage

from numpy.fft import fft2, ifft2
import numpy as np

pic= io.imread('cman.tif')
"""
mask1=np.zeros((3,3))
mask2=np.zeros((3,3))
mask1[1,0]=1; mask1[1,2]=-1
mask2[0,1]=1; mask2[2,1]=-1

c1=signal.convolve2d(pic, mask1, mode='full', boundary='fill', fillvalue=0)
c2=signal.convolve2d(pic, mask2, mode='full', boundary='fill', fillvalue=0)
"""
pic=pic.astype(float)

mask1=np.array([[1,0,-1]])
mask2=np.array([[1],[0],[-1]])

mask1=mask1.astype(float)
mask2=mask2.astype(float)

c1=ndimage.convolve(pic,mask1)
c2=ndimage.convolve(pic,mask2)

#io.imshow(c1)
#io.imshow(c2)
I1=c1.astype(float)
I2=c2.astype(float)

G=np.sqrt(np.square(I1)+np.square(I2))

#acc= I2/(I1+0.0000000001)
#theta= np.arctan(acc)
theta= np.arctan2(I2,I1)
mod_G=G.astype(np.uint16)

theta_deg= np.rad2deg(theta)
r,c = np.shape(theta_deg)


for i in range(0,r):
    for j in range(0,c):
        if theta_deg[i,j]<0:
            theta_deg[i,j]=theta_deg[i,j]+360
            

r,c = np.shape(theta_deg)
f_theta=np.zeros((r,c,3),dtype=np.uint8)

for i in range(0,r):
    for j in range(0,c):
        if (theta_deg[i,j]>=0) and (theta_deg[i,j]<40) :
            f_theta[i,j,0]=255
            f_theta[i,j,1]=0
            f_theta[i,j,2]=0
            
        elif (theta_deg[i,j]>=40) and (theta_deg[i,j]<80):
            f_theta[i,j,0]=255
            f_theta[i,j,1]=128
            f_theta[i,j,2]=0
           
        elif (theta_deg[i,j]>=80) and (theta_deg[i,j]<120):
            f_theta[i,j,0]=255
            f_theta[i,j,1]=255
            f_theta[i,j,2]=0
            
        elif (theta_deg[i,j]>=120) and (theta_deg[i,j]<160):
            f_theta[i,j,0]=0
            f_theta[i,j,1]=128
            f_theta[i,j,2]=255
            
        elif (theta_deg[i,j]>=160) and (theta_deg[i,j]<200):
            f_theta[i,j,0]=0
            f_theta[i,j,1]=255
            f_theta[i,j,2]=255
            
        elif (theta_deg[i,j]>=200) and (theta_deg[i,j]<240):
            f_theta[i,j,0]=0
            f_theta[i,j,1]=0
            f_theta[i,j,2]=255          
        elif (theta_deg[i,j]>=240) and (theta_deg[i,j]<280):
            f_theta[i,j,0]=0
            f_theta[i,j,1]=0
            f_theta[i,j,2]=255
        elif (theta_deg[i,j]>=280) and (theta_deg[i,j]<320):
            f_theta[i,j,0]=128
            f_theta[i,j,1]=0
            f_theta[i,j,2]=255
        elif (theta_deg[i,j]>=320) and (theta_deg[i,j]<360):
            f_theta[i,j,0]=255
            f_theta[i,j,1]=0
            f_theta[i,j,2]=255
            
            


io.imshow(f_theta)
































