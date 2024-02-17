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


def Delete_Word(Word):
    flag = False  
    
    try:
        with open('Windows/Study_Set/active_set.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: File 'active_set.json' not found.")
        return False
    except json.decoder.JSONDecodeError:
        print("Error: 'active_set.json' contains invalid JSON data.")
        return False
    
    # Create a copy of the data list to iterate over
    data_copy = data.copy()
    
    for item in data_copy:
        if item.get("Word") == Word:
            flag = True
            data.remove(item)  # Remove the item from the original data list
            break
    
    with open('Windows/Study_Set/active_set.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return flag

    
