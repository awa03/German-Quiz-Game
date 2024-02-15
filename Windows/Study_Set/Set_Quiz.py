import dearpygui.dearpygui as pygui
import Settings.Fonts as fonts
import Windows.Study_Set.Get_Set_Word as set_word

global current_window
def Start():
    global current_window
    word = set_word.Get_Rand_Word() 
    with pygui.window(label="Study Set", tag="Study Set", on_close=Exit ,width=1000, height=950):
        current_window = "Study Set"
        pygui.add_button(label="See Definition", callback=See_Definition, parent="Study Set")
        pygui.add_button(label="Next Word", callback=Next_Word, parent="Study Set")

        pygui.add_text(word, parent="Study Set", tag="Word")
          
def See_Definition():
    word = pygui.get_value("Word")
    definition = set_word.Get_Definition(word)
    pygui.add_text(definition, parent="Study Set", tag="Definition")

def Next_Word():
    pygui.delete_item("Word")
    word = set_word.Get_Rand_Word()
    pygui.add_text(word, parent="Study Set", tag="Word")
    pygui.delete_item("Definition")

def Exit():
    global current_window
    pygui.delete_item(current_window)

