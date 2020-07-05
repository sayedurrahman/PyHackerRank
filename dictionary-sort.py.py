# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 07:38:34 2020

@author: Sayedur Rahman(sayedur.rahmans@gmail.com)
Problem: 
Dictionary sort
"""

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print("Dictionary")
print(verse_dict, '\n')

# find number of unique keys in the dictionary
print("Dictionary unique keys")
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
print("Does dictionary contains key 'breathe'")
contains_breathe = verse_dict.get('breathe')
print(contains_breathe)

# create and sort a list of the dictionary's keys
print("Dictionary sort by sorted function")
sorted_dict= sorted(verse_dict)
print(sorted_dict)

print("Dictionary key sort by list sort")
sorted_keys = list(verse_dict.keys())
sorted_keys.sort()
# get the first element in the sorted list of keys
#print(sorted_keys[0])
print(sorted_keys[0])

# find the element with the highest value in the list of keys
#print(sorted_keys[-1]) 
print(sorted_keys[-1])