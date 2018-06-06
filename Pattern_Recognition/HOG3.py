#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 12:16:14 2018

@author: raja
"""


from skimage import io 
from skimage import color
from matplotlib import pyplot as plt
import numpy as np
import make_8
import raja

    from scipy import ndimage
    
    

raja1= io.imread('/home/raja/Mod 7/test pics/raja1.jpeg')
raja1=color.rgb2gray(raja1)*255

raja2= io.imread('/home/raja/Mod 7/test pics/car2.bmp')
#raja2=color.rgb2gray(raja2)*255
#raja2=np.zeros(np.shape(raja1))
#raja1=np.ones(np.shape(raja1))

raja3=raja1[500:800,450:850]
#raja2=raja1[900:1200,450:850]
raja1=np.copy(raja3)
raja2=np.copy(raja3)



rr1=make_8.put_color(raja1)
rr2=make_8.put_color(raja2)
r3=np.copy(rr1)+1
r4=np.copy(rr2)+1
r_1=make_8.make_8(r3)
r_2=make_8.make_8(r4)


num=np.sum(r_1*r_2)
den=np.sqrt(np.sum(r_1*r_1)) * np.sqrt(np.sum(r_2*r_2)) 
num1=r_1*r_2
cos= num/den
cos2=num1/den












