# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:02:58 2025

@author: ENG Khaled Elsafy
"""

umber_of_runs = 0
total_time = 0

while True:
    A = input("Enter 10 km run time: ")
    
    if A == "" or A == "0":
        break
    
    if A.replace('.', '', 1).isdigit():
        run_time = float(A)
        total_time += run_time
        number_of_runs += 1
    else:
        print("Invalid input!!. Please enter a  number* .")

average = total_time / number_of_runs
print(f"Average of {average}, over {number_of_runs} runs")