import Windows.Study_Set.Add_New_Words as Add_New_Words
import dearpygui.dearpygui as pygui
is_open = False
def Start():
    global is_open
    if is_open:
        return
    is_open = True
    with pygui.window(label="Add Words",
                      tag="Add Words",
                      width=500,
                      height=200,
                      no_collapse=True,
                      no_title_bar=True,
                      no_resize=True,
                      no_move=True,
                      on_close=Close_Window,
                      no_scrollbar=True,
                      no_scroll_with_mouse=True,
                      pos=(775, 40)
                      ):
        pygui.add_input_text(label="Word",
                             tag="Word_To_Add",
                             default_value="Word",
                             width=490,
                             height=50,
                             pos=(5, 5)
                             )
        pygui.add_input_text(label="Definition",
                             tag="Definition_To_Add",
                             default_value="Definition",
                             width=490,
                             height=50,
                             pos=(5,40)
                             )
        pygui.add_button(label="Add",
                         callback=Add_Word,
                         width=490,
                         height=40,
                         pos=(5, 75)
                         )
        pygui.add_button(label="Cancel",
                         callback=Close_Window,
                         width=490,
                         height=75,
                         pos=(5, 118)
                         )

def Add_Word():
    Word = pygui.get_value("Word_To_Add")
    Definition = pygui.get_value("Definition_To_Add")
    Add_New_Words.Add_Word(Word, Definition)
    with pygui.window(
        label="Added",
        tag="Added",
        width=490,
        height=70,
        pos=(775, 40),
        no_collapse=True,
        no_resize=True,
        no_move=True,
        no_scrollbar=True,
        no_title_bar=True
    ):
        pygui.add_text(
                "Word Added",
                parent="Added"
        )
        pygui.add_button(label="OK",
                         callback=Close_Added_Window,
                         parent="Added"
        )


    Close_Window()

def Close_Window():
    global is_open 
    is_open = False
    pygui.delete_item("Add Words")

def Close_Added_Window():
    pygui.delete_item("Added")

