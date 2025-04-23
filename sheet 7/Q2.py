# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:46:55 2025

@author: ENG Khaled Elsafy
"""

import numpy as np
# 6:
array_2d = np.arange(1, 10).reshape(3, 3)
print(array_2d)

print("\n***************************************************************************\n")

# 7:
array_1d = array_2d.flatten()  
print(array_1d)

print("\n***************************************************************************\n")

# 8:
my_array = np.arange(100)  
new_array = my_array.reshape(4, -1)  
print(new_array)

print('The Shape Is: ',  new_array.shape)