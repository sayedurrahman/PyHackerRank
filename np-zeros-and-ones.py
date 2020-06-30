# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 05:54:42 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
"""

import numpy

n=tuple([int(x) for x in input().split()])
print(numpy.zeros((n),dtype=int))
print(numpy.ones((n),dtype=int))