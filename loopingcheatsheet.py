# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:03:52 2019

@author: Patrick
"""

names = ['Patrick', 'Kawira', 'Mwenda', 'Fred', 'Kamau', 'Kaunde']
#looping over a single list

for name in names:
    print(name)
    
print("********Name and Index******")

for i in range(len(names)):
    print("{}:{}".format(i+1,names[i]))#i+1 start from 1 not 0

print("******Enumerate for name and index******")    
#Loop over a list while keeping track of indexes with enumerate
for indx,name in enumerate(names,start=1):
    print("{}:{}".format(indx,name))

print("********Reading from two lists********")

ratios = [0.1,0.5,0.3,0.9,0.8,0.7]
for i, name in enumerate(names):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, name))
    

#zip function allows us to loop over
# multiple lists at the same time
print("******easily join to lists using zip******")

for ratio, name in zip(ratios, names):
    print("{}% {}".format(ratio * 10, name))


#or
#note we go by shorter list

headers = ['Kenya', 'uganda', 'Ethiopia', 'Britain']
rows = ['Nairobi', 'Kampala', 'Addis Ababa']

for header, row in zip(headers, rows):
    print("{}: {}".format(header, ",".join(row)))



