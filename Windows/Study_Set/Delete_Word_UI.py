import dearpygui.dearpygui as pygui 
import json
import Windows.Study_Set.Add_New_Words as Add_New_Vals_Func
is_open = False
def Start():
    global is_open
    if is_open:
        return
    is_open = True
    with pygui.window(
        label="Delete Vals", 
        tag="Delete Vals", width=500, 
        height=200, on_close=Close_Window, 
        pos=(775, 40), no_collapse=True, no_resize=True,
        no_move=True, no_scrollbar=True, no_title_bar=True
    ):
        pygui.add_input_text(tag="Val",
                             width=490,
                             height=50,
                             pos=(5, 5)
        )
        pygui.add_button(label="Delete",
                         callback=Delete_Val,
                         width=490,
                         pos=(5, 40),
                         )
        pygui.add_button(label="Cancel",
                         callback=Close_Window,
                         width=490,
                         height=30,
                         pos=(5, 75),
                         )

def Delete_Val():
    Val = pygui.get_value("Val")

    with pygui.window(
        label="Error",
        tag="Error",
        width=490,
        height=70,
        pos=(780, 135),
        no_collapse=True,
        no_resize=True,
        no_move=True,
        no_scrollbar=True,
        no_title_bar=True
    ):
        if not Add_New_Vals_Func.Delete_Word(Val):
            pygui.add_text("Word not found",
                           parent="Error"
            )
            pygui.add_button(
                label="OK",
                callback=Close_Error_Window,
                parent="Error",
                width=490,
                height=50
            )

        else:
            pygui.add_text(
                "Word Deleted",
                parent="Error"
        )
            pygui.add_button(label="OK",
                             callback=Close_Error_Window,
                             parent="Error"
            )

def Close_Window(sender, data):
    global is_open
    is_open = False
    pygui.delete_item("Delete Vals")

def Close_Error_Window(sender, data):
    pygui.delete_item("Error")

