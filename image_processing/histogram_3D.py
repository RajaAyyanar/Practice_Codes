#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:12:35 2018

@author: raja
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

RGBlist = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for i in range(100)]
paleta=np.array(RGBlist)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(paleta[:,0],paleta[:,1],paleta[:,2], c=[(r[0] / 255., r[1] / 255., r[2] / 255.) for r in RGBlist])
ax.grid(False)
ax.set_title('grid on')
plt.savefig('blah.png')