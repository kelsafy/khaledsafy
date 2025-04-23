# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:26:33 2025

@author: ENG Khaled Elsafy
"""

def substitute(equation, **kwargs):
    for A, B in kwargs.items():
        equation = equation.replace(A, str(B))
    return equation

The_equation =substitute("A + 4 - B + 3 * z", A=7, B=8, C=6)
print(The_equation)