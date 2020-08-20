# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 04:15:23 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a_set=set(arr)
    print(sorted(a_set,reverse=True)[1])