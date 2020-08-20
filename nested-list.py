# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:40:14 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/nested-list/problem
"""

if __name__ == '__main__':
    d=dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in d:
            d[score].append(name)
        else:
            d[score]=list([name])
    second_key= sorted(d.keys())[1]
    for i in sorted(d[second_key]):
        print(i)