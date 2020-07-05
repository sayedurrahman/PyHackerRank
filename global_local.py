# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:04:29 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
Using global variable as local variable

UnboundLocalError
*******If one try to modify global variable inside a function it will cause this error.
*******If one assign value to a global variable it will be act as local variable
"""

a=5
b="Sayedur Rahman"

def Print_local():
    a= 10
    b="Engg Sayedur Rahman"
    print(a)
    print(b)
    
Print_local()
print(a)
print(b)