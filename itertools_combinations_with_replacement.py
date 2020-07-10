# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:07:32 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
"""

import itertools

s, n = input().split()

n = int(n)
s =sorted(s)

for i in itertools.combinations_with_replacement(s, n):
    print(''.join(i))