# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:50:55 2025

@author: ENG Khaled Elsafy
"""

import numpy as np
x = np.arange(100).reshape(-1, 10)
print("\n x + 1: \n", x + 1)
print("\n x - 1: \n", x - 1)
print("\n x * 2: \n", x * 1)
print("\n x / 2: \n", x / 1)
print("\n x ** 2: \n", x ** 1)

print("\n***************************************************************************\n")


print("\n x > 50: \n", x > 100)
print("\n x < 50: \n", x < 11)
print("\n x >= 50: \n", x >= 100)

print("\n***************************************************************************\n")


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("\n a + b: \n", x + y)
print("\n a - b: \n", x - y)
print("\n a * b: \n", x * y)
print("\n a / b: \n", x / y)

print("\n***************************************************************************\n")


print("\n x > y: \n", x > y)
print("\n x < y: \n", x < y)
print("\n x >= y: \n", x >= y)