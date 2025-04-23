# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:24:33 2025

@author: ENG Khaled Elsafy
"""

Family_Names = ["Khaled", "Asmaa", "Mohamed", "Sahar", "Ahd"]
A = {char for name in Family_Names for char in name}
print("letters are used in family members :")
print(A)