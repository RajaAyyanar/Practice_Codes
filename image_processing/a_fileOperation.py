#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 00:32:32 2018

@author: raja
"""


from os import listdir
from os.path import isfile, join

k=listdir('/home/raja/mod5_assignment/single/')

onlyfiles = [f for f in listdir('/home/raja/mod5_assignment/single/') if isfile(join('/home/raja/mod5_assignment/single/', f))]


import os

inpath= "/home/raja/mod5_assignment/database/AlphaNumeric/"
out=listdir(inpath)
for i in out:
    
    dirPath = "/home/raja/mod5_assignment/database/AlphaNumeric/%s" %(i)
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        #os.remove(dirPath+"/"+fileName)






