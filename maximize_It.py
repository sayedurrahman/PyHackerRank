# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:47:08 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/maximize-it/problem
"""

import itertools

k,m=map(int, input().split())

def get_value(arr):
    return sum([pow(a,2) for a in arr]) % m

# generate the 2D array
arr = [[int(x) for x in input().split()[1:]] for _ in range(k)]

# break into all combinations
value_list = [get_value(element) for element in itertools.product(*arr)]

print(max(value_list))
