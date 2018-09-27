#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:09:24 2018

stri="2323:3243434"
re.sub(r'.*:', '0', stri)
@author: raja
"""

import pandas as pd
import re
import os, glob
import numpy as np

df= pd.read_csv("/home/raja/chem/data3/data1.csv", sep=',',header=None)

target=df[0]
features=df.drop([0], axis=1)



path = "/home/raja/chem/data3/"                 # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent

df_from_each_file = (pd.read_csv(f, sep=',', header=None) for f in all_files)
c_df   = pd.concat(df_from_each_file, ignore_index=True)

r,c = np.shape(c_df)

k=[]
for i in range(0,c):
    if i%2 == 0:
        k.append(i)
        
        
new=c_df[k]

new.to_csv('final_data.csv',index=False,header=False)
