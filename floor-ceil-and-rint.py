# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 02:24:09 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem:
https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
"""
import numpy
numpy.set_printoptions(legacy='1.13')

array = numpy.array(input().split(), dtype=float)
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))

