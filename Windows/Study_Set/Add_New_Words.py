# Add words to active vocabulary
# FILE: active_set.json
import json
import sys
def Add_Word(Word, Definition):
    try:
        with open('Windows/Study_Set/active_set.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
        
    data.append({"Word": Word, "Definition": Definition})
    
    with open('Windows/Study_Set/active_set.json', 'w') as f:
        json.dump(data, f, indent=2)

