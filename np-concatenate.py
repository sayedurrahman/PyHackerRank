# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 04:55:02 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/np-concatenate/problem
"""

import numpy

n,m,p=map(int, input().split())

def convert_to_ints(arr):
    return [int(x) for x in arr]
        
first_array = [convert_to_ints(x) for x in (input().split() for x in range(n))]
second_array = [convert_to_ints(x) for x in (input().split() for x in range(m))]

print(numpy.concatenate([first_array,second_array]))