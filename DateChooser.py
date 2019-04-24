# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:28:33 2019

@author: Josh
"""
import random
import csv

file = open("DateIdeas.csv")
numline = len(file.readlines())

with open('DateIdeas.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    
dateIdea = random.randint(1, (numline-1))
print((rows[dateIdea]))