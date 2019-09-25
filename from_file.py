# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:00:56 2019

@author: Patrick
"""
from collections import Counter

with open('hello.txt') as my_file:
    lines = list(my_file)

#print(lines)

word_count = Counter(open('hello.txt').read().splitlines())

#print(word_count)
with open('hello.txt') as m_file:
    for line in m_file:
        if 'z' in line:
            print("z word", line, end = '')
        else:
            print("No z word found")
