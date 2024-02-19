import dearpygui.dearpygui as pygui
import os
import Settings.Fonts as fonts
import Windows.Study_Set.Get_Set_Word as set_word
import Windows.Study_Set.Set_Manager as manager


global current_window
global is_def_shown
instance = manager.SetManager()
current_directory = os.getcwd()
file_path = f'Window/Study_Set/{instance.active_set}'

# For Line Wrapping
def add_newline(string):
    words = string.split()
    if len(words) <= 5:
        return string
    else:
        new_string = ''
        for i, word in enumerate(words):
            new_string += word + ' '
            if (i + 1) % 10 == 0:
                new_string += '\n'
        return new_string.strip()

def Start():
    global current_window
    global is_def_shown
    is_def_shown = False
    word = set_word.Get_Rand_Word() 
<<<<<<< Updated upstream
    with pygui.window(label="Study Set", tag="Study Set", on_close=Exit ,width=1000, height=950):
        current_window = "Study Set"
        pygui.add_button(label="See Definition", callback=See_Definition, parent="Study Set")
        pygui.add_button(label="Next Word", callback=Next_Word, parent="Study Set")

        pygui.add_text(word, parent="Study Set", tag="Word")
          
=======
    word = add_newline(word)
    print(word)
    with pygui.window(label="Study Set",
                      tag="Study Set",
                      no_collapse=True,
                      no_resize=True,
                      no_move=True,
                      no_scrollbar=True,
                      no_title_bar=True,
                      on_close=Exit ,
                      width=700,
                      height=500,
                      pos=(580, 35)
    ):
        current_window = "Study Set"
        pygui.add_button(label="See Definition",
                         callback=See_Definition,
                         parent="Study Set",
                         width=700,
                         height=100
        )
        pygui.add_button(label="Next Word",
                         callback=Next_Word,
                         parent="Study Set",
                         width=700,
                         height=100
        )

        Word_Active_In_Set = pygui.add_text(word,
                       parent="Study Set",
                       tag="Word_In_Set",
        )
        pygui.add_button(label="Close",
                         callback=Exit,
                         width=700,
                         height=50,
                         pos=(0, 440),
                         )
>>>>>>> Stashed changes
def See_Definition():
    global is_def_shown
    if not is_def_shown:
        is_def_shown = True
        word = pygui.get_value("Word")
        definition = set_word.Get_Definition(word)
<<<<<<< Updated upstream
        pygui.add_text(definition, parent="Study Set", tag="Definition")
=======
        definition = add_newline(definition)
        pygui.add_text(definition,
                       parent="Study Set",
                       tag="Definition_In_Set",
        )
>>>>>>> Stashed changes

def Next_Word():
    global roboto
    global is_def_shown
    is_def_shown = False
    pygui.delete_item("Word")
    word = set_word.Get_Rand_Word()
    pygui.add_text(word, parent="Study Set", tag="Word")
    pygui.delete_item("Definition")

def Exit():
    global current_window
    pygui.delete_item(current_window)

