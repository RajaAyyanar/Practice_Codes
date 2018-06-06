#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:46:46 2018

@author: raja
"""

import os
from skimage import io,color
import numpy as np

def tex_data():    
    inpath= "/home/raja/Mod 7/texture"
    all_5=['T24_corduroy', 'T17_glass2', 'T20_upholstery']#, 'T03_bark3', 'T18_carpet1']
    
    
    x_data=[]
    y_fullName=[]
    y_target=[]
    
    
    status=0
    for i in all_5:
        status+=1
        print(status)
        dirPath = inpath+"/%s" %(i)
        fileList = os.listdir(dirPath)
        
        for fileName in fileList:
            
            pic= io.imread(dirPath+'/'+fileName, as_grey=True)
            x_data.append(pic)
            y_fullName.append(fileName)
            y_target.append(i)
            
            
    X=x_data
    y=y_target
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=2,shuffle=True)
    return X_train, X_test, y_train, y_test



        
        
        
        