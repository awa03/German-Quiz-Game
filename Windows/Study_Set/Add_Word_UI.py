import Windows.Study_Set.Add_New_Words as Add_New_Words
import dearpygui.dearpygui as pygui

def Start():
    with pygui.window(label="Add Words", tag="Add Words", width=500, height=500, on_close=Close_Window):
        pygui.add_input_text(label="Word", tag="Word", width=200)
        pygui.add_input_text(label="Definition", tag="Definition", width=200)
        pygui.add_button(label="Add", callback=Add_Word)

def Add_Word():
    Word = pygui.get_value("Word")
    Definition = pygui.get_value("Definition")
    Add_New_Words.Add_Word(Word, Definition)
    Close_Window()

def Close_Window():
    pygui.delete_item("Add Words")
