# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 06:01:09 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem:
https://www.hackerrank.com/challenges/np-inner-and-outer/problem
"""

import numpy

array_1=numpy.array(input().split(),dtype=int)
array_2=numpy.array(input().split(),dtype=int)

print(numpy.inner(array_1,array_2))
print(numpy.outer(array_1,array_2))


