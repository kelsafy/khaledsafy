# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:49:31 2025

@author: ENG Khaled Elsafy
"""

import numpy as np

array= np.arange(0, 1.1, 0.1)
print(array)

print("\n***************************************************************************\n")

X = np.arange(100).reshape(-1, 10)
print(X)

double_X = X.astype('float64')  
print(double_X)