# Add words to active vocabulary
# FILE: active_set.json
import json
import sys
import os
import Windows.Study_Set.Set_Manager as manager

is_open = False
instance = manager.SetManager()
current_directory = os.getcwd()
file_path = f'Windows/Study_Set/{instance.active_set}'

def Add_Word(Word, Definition):
    Update_Set()
    global current_directory
    print(current_directory + "\n\n")
    global file_path
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
        
    data.append({"Word": Word, "Definition": Definition})
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def Delete_Word(Word):
    Update_Set()
    global file_path
    flag = False  
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return False
    except json.decoder.JSONDecodeError:
        print(f"Error: '{file_path}' contains invalid JSON data.")
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

def Update_Set():
    # Set Curr Dir to home dir
    global file_path
    global instance
    instance = manager.SetManager()
    file_path = os.path.join('Windows/Study_Set', instance.active_set)


    


