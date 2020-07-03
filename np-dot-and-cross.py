# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 05:40:30 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem:
https://www.hackerrank.com/challenges/np-dot-and-cross/problem
"""

import numpy

n= int(input())
array_1=numpy.array([input().split() for i in range(n)],dtype=int)
array_2=numpy.array([input().split() for i in range(n)],dtype=int)
print(numpy.dot(array_1,array_2))
