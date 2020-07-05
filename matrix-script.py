# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:32:40 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
https://www.hackerrank.com/challenges/matrix-script/problem

****************Decode Without if condition***************

"""

#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    new = []
    for i in matrix_item:
        new.append(i)
    matrix.append(new)

transpose=[*zip(*matrix)]

cipher_str =''.join([''.join(i) for i in transpose])

string_head=0
output=""
pattern='[a-zA-Z0-9][\s!@#$%&]+[a-zA-Z0-9]'
p=re.compile(pattern)
for match in p.finditer(cipher_str):
    s = match.start()
    e = match.end()
    output+=cipher_str[string_head:s]+cipher_str[s]+" "+cipher_str[e-1]
    string_head=e

output+= cipher_str[string_head:]

print(output)