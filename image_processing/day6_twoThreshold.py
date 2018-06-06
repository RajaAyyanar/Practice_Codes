#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:44:35 2018

@author: raja
"""

from skimage import io,color
from skimage import data
import numpy as np
from matplotlib import pyplot as plt


#p= io.imread('test1.jpg')


sp=io.imread('spine.tif')

sp2= 255* color.rgb2gray(sp)


plt.hist(sp2.ravel(),255,[0,255]); plt.show()
plt.figure()

#t2=np.zeros((np.round(np.max(sp2),10))
#r=np.int(np.round(np.max(sp2)))
#t2=np.zeros((15,5))
#t3=np.zeros((15,5))


    
    
threshold= np.min(sp2)+1  
threshold2= np.max(sp2)-1  
t1= np.copy(threshold)
t2= np.copy(threshold2)

for j in range(0,20):
    print(t1,'  ',t2)
    m2= np.mean(sp2[np.nonzero(sp2>=t1)])
    m1= np.mean(sp2[np.nonzero(sp2<t1)])
    #print(m1,m2)
    
    w2= np.mean(sp2[np.nonzero(sp2>=t2)])
    w1= np.mean(sp2[np.nonzero(sp2<t2)])
    
    t1= (2*m1 + m2)/3
    t2= (w1 +2*w2)/3
    
    
    plt.imshow()
    
    """
plt.plot(t2[i])
plt.hold(True)



plt.show()


"""