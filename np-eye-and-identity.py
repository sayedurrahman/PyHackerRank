# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:59:55 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
    https://www.hackerrank.com/challenges/np-eye-and-identity/problem
"""

import numpy
numpy.set_printoptions(legacy='1.13')

n,m =map(int, input().split())
print(numpy.eye(n,m,k=0))
