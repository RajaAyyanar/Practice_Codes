#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 01:25:44 2018

@author: raja
"""

import os
from skimage import io,color

inpath= "/home/raja/mod5_assignment/Datasets/English_fnt_regionprobs/Capital_Letters"
#outpath="/home/raja/mod5_assignment/Datasets/English_fnt_regionprobs/"
out=os.listdir(inpath)
"""
x_train_data=[]
#y_train_data=[]
y_fullName=[]
y_name=[]
y_num=[]
"""
status=0
for i in out:
    status+=1
    print(status)
    dirPath = inpath+"/%s" %(i)
    fileList = os.listdir(dirPath)
    
    for fileName in fileList:
        
        pic= io.imread(dirPath+'/'+fileName, as_grey=True)
        x_train_data.append(pic)
        #y_train_data.append(i)
        
        name=str(fileName[3:6])
        num=int(name)
        y_fullName.append(fileName)
        y_name.append(name)
        y_num.append(num)