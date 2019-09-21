# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:33:38 2019

@author: Patrick
"""

#split function
course_id = "CSC 310"

#I want the number only
num = course_id.split()[-1]
#returns 310 as string, int(num) == integer

#*************************************************************

#list
#creating an empty list, numbers = list() - not recommended 
numbers = []
numbers = [10, 25, 60,48, 75]
copy_of_numbers = numbers.copy()
num_squares = [n**2 for n in numbers]

#print(num_squares)

#**********************************************************

#converting a list into tuple
nums = tuple(numbers)
#print(nums)

#**********************************************************

#dictionary function
#dict also accept another dictionary my_dict2 = dict(my_dict)
#converting a tuple into a dictionary
tup_list = [('red', 2),('black', 5),('blue', 8),('pink', 4)]

my_dict = {}#best practice to create dict
my_dict = dict(tup_list)

another_dict = {'KE':'Nairobi', 'UG':'Kampala', 'TZ':'Dodoma'}
#print(another_dict)

#looping through a dictionary
"""
for key in another_dict:
    print(key)
    
    """
    
#or
"""
for key in another_dict:
    print(key,"->", another_dict[key])
"""
#or using items()
"""
for key in my_dict.items():
    print(key)
"""
for key, value in my_dict.items():
    print(key,":",value)

