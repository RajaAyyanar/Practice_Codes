#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 23:26:47 2018

@author: raja
"""

import mahotas as mh
img = np.array(img)
im = img[:,0:50,0]
im = im < 128
skel = mh.thin(im2)
noholes = mh.morph.close_holes(skel)
plt.subplot(311)
plt.imshow(im)
plt.subplot(312)
plt.imshow(skel)
plt.subplot(313)
cskel = np.logical_not(skel)
choles = np.logical_not(noholes)
holes = np.logical_and(cskel,noholes)
lab, n = mh.label(holes)
print 'B has %s holes'% str(n)
plt.imshow(lab)