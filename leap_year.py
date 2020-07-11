# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:20:39 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/write-a-function/problem
"""

def is_leap(year):
    leap = False
    
    if (year % 4 == 0):
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    
    return leap

year = int(input())
print(is_leap(year))