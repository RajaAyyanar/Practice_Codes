#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 12:19:14 2018

@author: raja
"""

from sklearn import datasets
import pandas as pd
import numpy as np
from skimage import io,color
from matplotlib import pyplot as plt

iris = datasets.load_iris()
X = iris.data[:, :4]  
y = iris.target


df = pd.read_csv('/home/raja/iris.csv')
x_all=np.array(df.iloc[:,0:4])
y_all=np.array(df.iloc[:,4])

r,c= np.shape(X)

winsize =10
wininc=5
st=0
en=winsize
datasize=r
Nsignals=c

numwin = np.floor((datasize-winsize)/wininc)+1
feat = np.zeros((np.int(numwin),Nsignals))
tar = np.zeros((np.int(numwin)))

numwin=numwin.astype(int)
for i in range(0,numwin):
    curwin = X[st:en, :]
    curtar= y[st:en]
    feat[i,:] = np.sqrt(np.mean(curwin**2, axis=0))
    tar[i]=np.sqrt(np.mean(curtar**2, axis=0))
    st=st+wininc
    en= en + wininc
    
plt.plot(X);
plt.figure()
plt.plot(feat)


