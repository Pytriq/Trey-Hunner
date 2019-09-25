# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:18:44 2019

@author: Patrick
"""

#List comprehensions are a tool for transforming one list
# (any iterable actually) into another list.

# create a list2 of double odds from list1


list1 = [2, 45, 75, 56, 24, 89, 36, 80]

"""
unconditional list comprehension
"""
list2 = [n for n in list1]
#or just
list2 = list(list1)

"""
conditional list comprehension
"""
#for loop
#list2 = []
#for n in list1:
#    if n % 2 == 0:
#        list2.append(n*2)
#print(list2)

list2 = [n*2 for n in list1 if n % 2 == 0]
#print(list2)

#nested for loop
#flatten = []
#for row in matrix:
#    for n in row:
#        flatten.append(n)
#listcomp
"""
nested list comprehension
"""   
#flatten = [n for row in matrix for n in row]

"""
set comprehension
"""
words = ['Patrick', 'James', 'Kenneth']
first_letters = set()
for letter in words:
    first_letters.add(letter[0])

#set comprehension
first_lettrs = {letter[0] for letter in words}
print(first_lettrs)

"""
dict comprehension
"""
#note, the dict() can easily replace dict compre
#eg
listp = [('IT','Italy'), ('KE','Kenya'), ('UG','Uganda')]
dicto = {abbr: country for abbr, country in listp }
#instead you could just
dictp = dict(listp)

#swap dictionary key and values
original = {'F':'Female', 'M':'Male', 'Q':'Queer'}
swapped = {}
for key, value in original.items():
    swapped[value]= key

#dict comp
swapped = {value: key for key, value in original.items()}

#Remember that Python allows 
#line breaks between brackets and braces.
#improved readability
swapped = {
        value: key
        for key, value in original.items()
        }
print(swapped)

