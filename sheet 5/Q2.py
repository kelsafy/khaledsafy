# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:29:00 2025

@author: ENG Khaled Elsafy
"""

A_coor = [1, 2, 3, 4, 5]
B_coor = [2, 4, 6, 8, 10]
C_coor = [0, -1, -2, -3, -4]

points = [(A, B, C) for A, B, C in zip(A_coor, B_coor, C_coor)]

print(points)