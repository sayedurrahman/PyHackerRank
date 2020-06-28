# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:49:47 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)

Problem:
https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
"""

import numpy

n, m=map(int, input().split())

arrs=numpy.zeros((n,m),int)

for i in range(n):
    arrs[i]=input().split()
    
print(numpy.transpose(arrs))
print(arrs.flatten())
