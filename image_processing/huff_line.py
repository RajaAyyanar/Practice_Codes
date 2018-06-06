#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:30:35 2018

@author: raja
"""

import numpy as np
from matplotlib import pyplot as plt


x1=np.array([[i for i in range(0,10)]])
y1=np.array([[i for i in range(0,10)]])

plt.plot(x1,y1,'r*')
plt.hold(True)


x2=np.array([[i for i in range(0,10)]])
y2=np.array([[i for i in range(0,10)]])
plt.plot(x1,y1,'b*')