# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 05:16:15 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
"""

import numpy
numpy.set_printoptions(legacy='1.13')

n,m= map(int, input().split())
array=numpy.array([input().split() for i in range(n)],dtype=int)

print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(numpy.std(array, axis=None))