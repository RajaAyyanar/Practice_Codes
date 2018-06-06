#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 00:10:00 2018

@author: raja
"""

import pickle
>>> foo=123
>>> bar="hello"
>>> d={'abc': 123, 'def': 456}
>>> f=open('p.pickle', 'wb')
>>> pickle.dump(foo, f)
>>> pickle.dump(bar, f)
>>> pickle.dump(d, f)



import pickle
>>> f=open('p.pickle','rb')
>>> foo=pickle.load(f)
>>> foo
123
>>> bar=pickle.load(f)
>>> bar
'hello'
>>> d=pickle.load(f)
>>> d
{'abc': 123, 'def': 456}
>>> 