import json
import random
import sys
# Get a set of words from a file
def Get_Set():
    
    with open('Windows/Study_Set/active_set.json', 'r') as file:
        data = json.load(file)
    return data

# Get a random word from the set
def Get_Rand_Word():
    # only return german 
    data = Get_Set()
    word = random.choice(data)
    return word['Word']

def Get_Definition(word):
    data = Get_Set()
    for item in data:
        if item['Word'] == word:
            return item['Definition']
