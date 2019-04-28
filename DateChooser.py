# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:28:33 2019

@author: Josh
"""
import random
import csv
import wget
import os.path

def Download_file():
    link_to_data = "https://raw.githubusercontent.com/JWoodbr/JustTheLittleThings/master/DateIdeas.csv"
    wget.download(link_to_data)



if os.path.isfile("DateIdeas.csv"):
    os.remove('DateIdeas.csv')
    Download_file()
else:
    Download_file()



file = open("DateIdeas.csv")
numline = len(file.readlines())
file.close()

with open('DateIdeas.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_file)
    
dateIdea = random.randint(1, (numline-1))
print((rows[dateIdea]))


#sort date ideas by cheap, summer, spring,expensive, etc
