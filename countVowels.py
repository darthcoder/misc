# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 20:19:27 2015

@author: abasit
"""

input = "This is a long string from where we will count the number of vowels"

def count(string):
    """Right now using a predefined string, this would be replaced by console
    input in the later stages"""
    counter = 0
    for letter in string:
        if letter in ['a','e','i','o','u']:
            counter = counter + 1
    print counter        
            
        
count(input)


