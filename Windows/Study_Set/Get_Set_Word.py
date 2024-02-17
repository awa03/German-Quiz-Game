import json
import random
import sys
import dearpygui.dearpygui as pygui
# Get a set of words from a file
is_open_view_flash = False

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

def view_all_words(sender, data):
    global is_open_view_flash
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
            with open('Windows/Study_Set/active_set.json', 'r') as f:
                data = json.load(f)
                
            for item in data:
                pygui.add_text(f"Word: {item['Word']}, Definition: {item['Definition']}",
                               parent="Word Viewer"
                               )
                
        except FileNotFoundError:
            pygui.add_text("File 'active_set.json' not found",
                           parent="Word Viewer")
        except json.decoder.JSONDecodeError:
            pygui.add_text("'active_set.json' contains invalid JSON data.",
                           parent="Word Viewer")
        pygui.add_button(label="Close",
                         callback=close_word_viewer,
                         width=672,
                         height=50
                         )


def close_word_viewer(sender, data):
    global is_open_view_flash
    is_open_view_flash = False
    pygui.delete_item("Word Viewer")
