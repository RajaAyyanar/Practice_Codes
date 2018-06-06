#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 12:11:39 2018

@author: raja
"""

import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import datasets
import sklearn
#from sklearn.cross_validation import train_test_split


iris = datasets.load_iris()
X = iris.data
y = iris.target


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=1,shuffle=True)


lda_clf = LinearDiscriminantAnalysis(solver = 'lsqr').fit(X_train,y_train)
#post_probs = lda_clf.predict_proba(X_test)
y_pred = lda_clf.predict(X_test)

from sklearn import metrics
print("LDA model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)


confusion1=sklearn.metrics.confusion_matrix(y_test, y_pred, labels=None, sample_weight=None)
