# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:37:44 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/itertools-combinations/problem
"""

import itertools

s, n = input().split()

n = int(n)
s =sorted(s)
count = 1

while count < n+1 :  
    for i in itertools.combinations(s, count):
        print(''.join(i))
    count+=1