#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:15:01 2018

@author: raja
"""
import numpy as np

a = np.array([[1,5,9],[2,6,10]])
b = np.array([[3,7,11],[4,8,12]])
c=np.concatenate((a,b),axis=0)