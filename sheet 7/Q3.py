# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:48:10 2025

@author: ENG Khaled Elsafy
"""

import numpy as np

A= np.arange(100).reshape(-1, 10)  

B = A[9][2]
print(A)

print("\n***************************************************************************\n")


row3 = A[2, :]
print(row3)

print("\n***************************************************************************\n")


column4 = A[:, 3]
print(column4)