#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:44:50 2018

@author: raja
"""


import numpy as np
from skimage import io,color
import cv2
from matplotlib import pyplot as plt
import pandas as pd 
import calc_HOG

csv_path='/home/raja/Mod 7/Tiger2/groundtruth_rect.txt'
pic_path= '/home/raja/Mod 7/Tiger2/img/0010.jpg'
G_truth = np.genfromtxt(csv_path, delimiter=',')
G_truth= np.int64(G_truth)
pic= io.imread(pic_path)
a,b,c,d=G_truth[10,:]

y_tar=pic[b:b+d,a:a+c]
f1=calc_HOG.HOG_feat(y_tar)


pic_back=np.copy(pic)
pic_back[b:b+d,a:a+c]=0
row,col,dim= np.shape(pic)
feat=[]
for i in range(0,row-d):
    for j in range(0,col-c):
        temp=pic_back[i:i+d,j:j+c]
        feat.append(calc_HOG.HOG_feat(temp))