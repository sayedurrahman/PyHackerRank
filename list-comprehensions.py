# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 01:04:46 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

import itertools

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    x_all_elements=list(range(x+1))
    y_all_elements=list(range(y+1))
    z_all_elements=list(range(z+1))

    arr = itertools.product(x_all_elements,y_all_elements,z_all_elements)
    arr=[[a,b,c] for a, b, c in arr if (a+b+c) != n]
    print(list(arr))