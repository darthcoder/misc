# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 14:43:10 2015

@author: abasit
"""

input = "A string to be counted for the number of words"
count = 0

def wordCount(string):
    words = string.split()
    print len(words)

wordCount(input)
