#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 03:35:00 2018

@author: raja
"""

# import the necessary packages
from collections import namedtuple
import numpy as np
import cv2
 
# define the `Detection` object
Detection = namedtuple("Detection", ["image_path", "gt", "pred"])