# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:51:19 2019

@author: Patrick
"""

def prime_nums(number):
    for num in range(2, number):
        if num % 2 == 0:
            return False
    return True

#using the all generator function
    
def is_prime(number):
    return all(
            number % num != 0
            for num in range(2, number)
            )
