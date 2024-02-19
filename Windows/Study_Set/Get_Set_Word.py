import json
import random
import sys
import os
import Windows.Study_Set.Set_Manager as manager
import dearpygui.dearpygui as pygui
# Get a set of words from a file
instance = manager.SetManager()
file_path = os.path.join('Windows/Study_Set', instance.active_set)
is_open_view_flash = False

def Get_Set():
    Update_Set()
    global file_path
    with open(file_path, 'r') as file:
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

def view_all_words(sender, data):
    Update_Set()
    global file_path    
    global is_open_view_flash
    print (file_path + "\n\n")
    if is_open_view_flash:
        close_word_viewer(None, None)
    is_open_view_flash = True
    with pygui.window(label="Word Viewer",
                      tag="Word Viewer", width=700,
                      height=500,
                      on_close=close_word_viewer,
                      no_move=True,
                      no_resize=True,
                      no_scroll_with_mouse=True,
                      no_collapse=True,
                      no_title_bar=True,
                      no_close=True,
                      pos=(580, 35)
                      ):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            for item in data:
                pygui.add_text(f"Word: {item['Word']}, Definition: {item['Definition']}",
                               parent="Word Viewer"
                               )
                
        except FileNotFoundError:
            pygui.add_text(f"File '{file_path}' not found",
                           parent="Word Viewer")
        except json.decoder.JSONDecodeError:
            pygui.add_text(f"'{file_path}' contains invalid JSON data.",
                           parent="Word Viewer")
        pygui.add_button(label="Close",
                         callback=close_word_viewer,
                         width=672,
                         height=50
                         )


def Update_Set():
    # Set Curr Dir to home dir
    global file_path
    global instance
    instance = manager.SetManager()
    file_path = os.path.join('Windows/Study_Set', instance.active_set)

def close_word_viewer(sender, data):
    global is_open_view_flash
    is_open_view_flash = False
    pygui.delete_item("Word Viewer")
