#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 12:30:41 2018

@author: raja
"""

def make_8(pic):
        
    from skimage import io
    from matplotlib import pyplot as plt
    import numpy as np
    
    
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
            
              
    
    
    dd=np.zeros((r,c))
    k1=8;
    for i in range(0,r,8):
        k2=8
        for j in range(0,c,8):
            
            pic2= pic[i:i+k1,j:j+k2]
            dd[i:k1+i,j:k2+j]=boxx(pic2)
            
            
            
    return dd
            
            
def put_color(pic):
        
    from skimage import io
    from matplotlib import pyplot as plt
    from scipy import signal
    import numpy as np
    from scipy import ndimage
    
    
    
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
    d_theta=np.zeros((r,c),dtype=np.float)
    
    for i in range(0,r):
        for j in range(0,c):
            if (theta_deg[i,j]>=0) and (theta_deg[i,j]<40) :
                f_theta[i,j,0]=255
                f_theta[i,j,1]=0
                f_theta[i,j,2]=0
                d_theta[i,j]=0
                
            elif (theta_deg[i,j]>=40) and (theta_deg[i,j]<80):
                f_theta[i,j,0]=255
                f_theta[i,j,1]=128
                f_theta[i,j,2]=0
                d_theta[i,j]=1
                
            elif (theta_deg[i,j]>=80) and (theta_deg[i,j]<120):
                f_theta[i,j,0]=255
                f_theta[i,j,1]=255
                f_theta[i,j,2]=0
                d_theta[i,j]=2
                
            elif (theta_deg[i,j]>=120) and (theta_deg[i,j]<160):
                f_theta[i,j,0]=0
                f_theta[i,j,1]=128
                f_theta[i,j,2]=255
                d_theta[i,j]=3
                
            elif (theta_deg[i,j]>=160) and (theta_deg[i,j]<200):
                f_theta[i,j,0]=0
                f_theta[i,j,1]=255
                f_theta[i,j,2]=255
                d_theta[i,j]=4
                
            elif (theta_deg[i,j]>=200) and (theta_deg[i,j]<240):
                f_theta[i,j,0]=0
                f_theta[i,j,1]=0
                f_theta[i,j,2]=255     
                d_theta[i,j]=5
                
            elif (theta_deg[i,j]>=240) and (theta_deg[i,j]<280):
                f_theta[i,j,0]=0
                f_theta[i,j,1]=0
                f_theta[i,j,2]=255
                d_theta[i,j]=6
                
            elif (theta_deg[i,j]>=280) and (theta_deg[i,j]<320):
                f_theta[i,j,0]=128
                f_theta[i,j,1]=0
                f_theta[i,j,2]=255
                d_theta[i,j]=7
                
            elif (theta_deg[i,j]>=320) and (theta_deg[i,j]<360):
                f_theta[i,j,0]=255
                f_theta[i,j,1]=0
                f_theta[i,j,2]=255
                d_theta[i,j]=8
                
                
    
    
    return d_theta
    
