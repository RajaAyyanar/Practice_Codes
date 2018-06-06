#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:33:46 2018

@author: raja
"""
import numpy as np
import read_dir
import calc_HOG

X_train,X_test,y_train,y_test = read_dir.tex_data()

#CREATING Blocks of datasets for Training
max_X_train=[]
max_y_train=[]
for k in range(0,len(X_train)):
    print(k)
    one=X_train[k]
    one_y=y_train[k]
    pic=np.array(one)
    r,c = np.shape(pic)
    for i in range(0,r,32):
        for j in range(0,c,32):
            small_pic=pic[i:i+32, j:j+32]
            max_X_train.append(calc_HOG.HOG_feat(small_pic))
            max_y_train.append(one_y)
            

#CREATING Blocks of datasets for Testing
max_X_test=[]
max_y_test=[]
for k in range(0,len(X_test)):
    print(k)
    one=X_test[k]
    one_y=y_test[k]
    pic=np.array(one)
    r,c = np.shape(pic)
    for i in range(0,r,32):
        for j in range(0,c,32):
            small_pic=pic[i:i+32, j:j+32]
            max_X_test.append(calc_HOG.HOG_feat(small_pic))
            max_y_test.append(one_y)
            
max_X_train=np.array(max_X_train)
max_X_test=np.array(max_X_test)
max_y_train=np.array(max_y_train)
max_y_test=np.array(max_y_test)

X_train=max_X_train[:,0,:]
X_test=max_X_test[:,0,:]
y_train=max_y_train
y_test=max_y_test
            
        
# training the model on training set
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)
 
# making predictions on the testing set
y_pred = gnb.predict(X_test)
 
# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("Without PCA Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)



##WITH PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=100)
X_pca_train=pca.fit_transform(X_train, y=None)          
X_pca_test=pca.fit_transform(X_test, y=None)          
            

gnb.fit(X_pca_train, y_train)
 
# making predictions on the testing set
y_pred = gnb.predict(X_pca_test)
 
# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("With PCA Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)

            
            
            
            
            
            
            
            
            
            
