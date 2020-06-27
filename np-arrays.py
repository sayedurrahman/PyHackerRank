# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 04:21:31 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
"""

import numpy

def arrays(arr):
    np_arr= numpy.array(arr, dtype=float)
    return numpy.flip(np_arr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)