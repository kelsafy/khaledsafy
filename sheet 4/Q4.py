# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:26:24 2025

@author: ENG Khaled Elsafy
"""

def average(*numbers):
    if not numbers:
        return 0
    sum_of_num = sum(numbers)
    
    count_of_num = len(numbers)
    
    return sum_of_num / count_of_num

z=average(30, 45, 17, 23, 104)
print(z)