# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:32:40 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem:
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""

def print_rangoli(size):
    lines=[]    
    for i in range( size):
        last_char = 96+size
        padding='-'*(2*(size-i-1))
        char_part=chr(last_char)
        j=1
        while last_char>96 and i>=j:
            last_char-=1
            j+=1
            char_part=f"{char_part}-{chr(last_char)}"
        line=f"{padding}{char_part}{char_part[:-1][::-1]}{padding}"
        lines.append(line)
    
    lines.extend(reversed(lines[:-1]))
    print(*lines,sep='\n')

        


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)