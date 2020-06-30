# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:42:59 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/np-array-mathematics/problem
"""

import numpy
numpy.set_printoptions(legacy='1.13')

n,m=map(int, input().split())

def convert_to_ints(arr):
    return [int(x) for x in arr]
        
first_array = numpy.array([input().split() for x in range(n)],dtype=int)
second_array = numpy.array([input().split() for x in range(n)],dtype=int)

print(numpy.add(first_array,second_array))
print(numpy.subtract(first_array,second_array))
print(numpy.multiply(first_array,second_array))
print(first_array//second_array)
print(numpy.mod(first_array,second_array))
print(numpy.power(first_array,second_array))