# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 02:21:22 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/np-min-and-max/problem
"""
import numpy

n,m=map(int, input().split())

array=numpy.array([input().split() for i in range(n)],dtype=int)
a_min=numpy.min(array,axis=1)
a_max=numpy.max(a_min)
print(a_max)

