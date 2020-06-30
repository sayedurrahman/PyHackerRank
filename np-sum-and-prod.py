# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 02:22:54 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem:
https://www.hackerrank.com/challenges/np-sum-and-prod/problem
"""
import numpy

n,m=map(int, input().split())

array=numpy.array([input().split() for i in range(n)],dtype=int)
a_sum=numpy.sum(array,axis=0)
a_prod=numpy.prod(a_sum)
print(a_prod)
