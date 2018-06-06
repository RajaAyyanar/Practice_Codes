#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 15:18:39 2018

@author: raja
"""


import numpy as np

from sklearn import svm
from sklearn import datasets
import sklearn
#from sklearn.cross_validation import train_test_split


iris = datasets.load_iris()
X = iris.data
y = iris.target


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=2,shuffle=True)


svm1 = svm.SVC()
svm1.fit(X_test, y_test) 
#post_probs = lda_clf.predict_proba(X_test)
y_pred = svm1.predict(X_test)

from sklearn import metrics
print("SVM model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)


confusion1=sklearn.metrics.confusion_matrix(y_test, y_pred, labels=None, sample_weight=None)

