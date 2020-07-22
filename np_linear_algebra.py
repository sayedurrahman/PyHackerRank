# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 02:58:52 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem:
https://www.hackerrank.com/challenges/np-linear-algebra/problem
"""

import numpy
#numpy.set_printoptions(legacy='1.13')

n= int(input())
array_1=numpy.array([input().split() for i in range(n)],dtype=float)
det = numpy.linalg.det(array_1)
print(round(det, 2))
