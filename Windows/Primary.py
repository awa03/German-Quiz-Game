import dearpygui.dearpygui as pygui
import Windows.Quiz as quiz
import Settings.Fonts as fonts
# Primary Window

def Start():
    with pygui.window(label="Primary Window", tag="Primary Window", width=1000, height=1000, on_close=Menu_Exit):
        pygui.add_text("German Quizzr", parent="Primary Window")
        pygui.add_button(label="Start Quiz", callback=Start_Quiz, parent="Primary Window")

def Start_Quiz():
    quiz.Start()

def Menu_Exit():
    pygui.destroy_context() 


