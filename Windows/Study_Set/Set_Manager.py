# Singleton class to manage the active set
import dearpygui.dearpygui as pygui
import json
import os

current_directory = os.getcwd()
study_set_directory = "Windows/Study_Set"
is_open = False

class SetManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._active_set = "active_set.json"
        return cls._instance

    @property
    def active_set(self):
        return self._active_set

    @active_set.setter
    def active_set(self, value):
        self._active_set = value


# Path: Set_Manager.py
def Start():
    global is_open
    if is_open:
        return
    is_open = True
    Show_Sets()


def Show_Sets():
    global is_open
    global study_set_directory
    if is_open:
        return
    # Change directory if needed


    with pygui.window(label="Set Manager", tag="Set_Manager",
                      width=700, height=400,
                      pos=(580, 530),
                      no_close=True, no_collapse=True,
                      no_resize=True, no_move=True, no_title_bar=True,
    ):
        json_files = [f for f in os.listdir(study_set_directory) if f.endswith('.json')]
        
        pygui.add_text("Select a set to manage", parent="Set Manager", pos=(10, 0))
        pygui.add_listbox(items=json_files, callback=Set_Active_Set, 
                          width = 675,
                          parent="Set Manager", pos=(10, 50))
        pygui.add_button(label="X", callback=Close_Set_Manager, parent="Set Manager",
                         pos=(665, 5), width=30, height=30,)


def Set_Active_Set(sender, data):
    selected_set = pygui.get_value(sender)
    print("Selected set:", selected_set)
    SetManager().active_set = selected_set

def Close_Set_Manager():
    pygui.delete_item("Set_Manager")
    global is_open
    is_open = False
