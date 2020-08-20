# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:28:30 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem:
https://www.hackerrank.com/challenges/capitalize/problem
"""

import re

s='234asdf dfg 56gh 67 fghj 678 67g 67ghj 67 hghj'
s=s.title()
index=0
output=''
print(s)
for m in re.finditer('[0-9]+[A-Z]', s):
    output+=s[index:m.start()]
    index=m.start()
    while s[index].isdigit():
        output+=s[index]
        index+=1
    output+=s[index].lower()
    index+=1
        
output+=s[index:]
print(output)