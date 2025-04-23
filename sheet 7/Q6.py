# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:53:55 2025

@author: ENG Khaled Elsafy
"""

import numpy as np

X = np.array([1,2,3]).reshape(3,1)
Y = np.array([4,5,6]).reshape(1,3)

print(X + Y)