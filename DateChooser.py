import random
import csv
import wget
import os.path
import pandas as pd

def Download_file():
    link_to_data = "https://raw.githubusercontent.com/JWoodbr/JustTheLittleThings/master/DateIdeas.csv"
    wget.download(link_to_data)

def checkupdatefile():
    if os.path.isfile("DateIdeas.csv"):
        os.remove('DateIdeas.csv')
        Download_file()
    else:
        Download_file()
def numblines():
    file = open("DateIdeas.csv")
    numline = len(file.readlines())
    file.close()

data = pd.read_csv("DateIdeas.csv")
Idea = data['Idea']
cost = data['cost']
print(cost)




checkupdatefile()
with open('DateIdeas.csv') as csv_file:
    rows = list(csv_file)
    
dateIdea = random.randint(1, (numline-1))
print(dateIdea)
print((rows[dateIdea]))


#sort date ideas by cheap, summer, spring,expensive, etc
