#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:30:42 2018

@author: raja
"""

import dill                            #pip install dill --user
filename = 'globalsave1.pkl'
dill.dump_session(filename)

# and to load the session again:
dill.load_session(filename)
