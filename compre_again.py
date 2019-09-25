# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:49:55 2019

@author: Patrick
"""

list1 = [2, 45, 75, 56, 24, 89, 36, 80]

#using parenthesis to improve readability
list2 = [
        (n//2 if n % 2 == 0 else n*2)
        for n in list1
        ]
#print(list2)

#using functions in compr for readability
"""new_list = [
        odd_numbers(n)
        for n in list1
        ]
"""
#sum of squares comp

sum_of_squares = sum(n**2 for n in list1)
print(sum_of_squares)

