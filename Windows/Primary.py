import sys
import os
import dearpygui.dearpygui as pygui
import Windows.Quiz as quiz
import Settings.Fonts as fonts
import Windows.Menu_Bar.Menu as menu
import Windows.Study_Set.Set_Quiz as study_set
import Windows.Study_Set.Add_Word_UI as Add_Word_U
import Windows.Study_Set.Delete_Word_UI as Delete_Word_U
import Windows.Study_Set.Get_Set_Word as Get_Set_Word
sys.path.append('../Settings/')
import Settings.Score_Saver as Score_Saver
# Primary Window

def Start():
    with pygui.window(label="Primary Window",
                      tag="Primary Window",
                      width=1000, height=950,
                      on_close=Menu_Exit,
                      no_resize=True,
                      no_collapse=True,
                      no_scroll_with_mouse=True,
                      no_background=True
    ):
        center_widgets()
        #menu.Add_Menu_Bar("Settings")

def center_widgets():
    # Add font 
    with pygui.font_registry():
        roboto = pygui.add_font("Settings/Roboto/Roboto-Thin.ttf",
                                45
        )
    high_score = Score_Saver.Get_Score()
    widget_width = 500
    num_widgets = 6  # Number of buttons + High Score text

    # Calculate the top margin to center the widgets vertically
    top_margin = 20  # Adjust as needed based on desired spacing

    # Add spacing to center widgets vertically
    pygui.add_dummy(width=0, height=top_margin)

    # Add widgets
    Header = pygui.add_text(
        "German Quizzr",
        parent="Primary Window"
    )
    pygui.add_button(
        label="Start Quiz",
        callback=Start_Quiz,
        parent="Primary Window",
        width=widget_width,
        height=70
    )
    pygui.add_button(label="Loaded Set",
                     callback=Start_Study_Set,
                     parent="Primary Window",
                     width=widget_width,
                     height=70
    )
    pygui.add_button(label="Add Words",
                     callback=Add_Words,
                     parent="Primary Window",
                     width=widget_width,
                     height=70
    )
    pygui.add_button(label="Delete Words",
                     callback=Delete_Word,
                     parent="Primary Window",
                     width=widget_width,
                     height=70
    )
    pygui.add_button(label="View Words In Set",
                     callback=view_all_words,
                     parent="Primary Window",
                     width=widget_width,
                     height=70
    )
    pygui.add_text(f"High Score: {high_score}",
                   parent="Primary Window"
    )

    # Add spacing for bottom margin
    pygui.add_dummy(width=0,
                    height=top_margin
    )
    pygui.bind_item_font(Header,
                         roboto
    )
   


def Start_Quiz():
    quiz.Start()

def Start_Study_Set():
    study_set.Start()

def Add_Words():
    Add_Word_U.Start()

def Delete_Word():
    Delete_Word_U.Start()

def view_all_words(sender, data):
    Get_Set_Word.view_all_words(sender, data)

def Menu_Exit():
    pygui.destroy_context() 



