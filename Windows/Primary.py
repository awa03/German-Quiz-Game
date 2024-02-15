import sys
import dearpygui.dearpygui as pygui
import Windows.Quiz as quiz
import Settings.Fonts as fonts
import Windows.Menu_Bar.Menu as menu
import Windows.Study_Set.Set_Quiz as study_set
sys.path.append('../Settings/')
import Settings.Score_Saver as Score_Saver
# Primary Window

def Start():
    high_score = Score_Saver.Get_Score()
    with pygui.window(label="Primary Window", tag="Primary Window", width=1000, height=950, on_close=Menu_Exit):
        pygui.add_dummy(width=0, height=20)
        pygui.add_text("German Quizzr", parent="Primary Window")
        pygui.add_button(label="Start Quiz", callback=Start_Quiz, parent="Primary Window")
        pygui.add_button(label="Loaded Set", callback=Start_Study_Set,parent="Primary Window") 
        pygui.add_text(f"High Score: {high_score}", parent="Primary Window")
        menu.Add_Menu_Bar("Settings")

def Start_Quiz():
    quiz.Start()

def Start_Study_Set():
    study_set.Start()

def Menu_Exit():
    pygui.destroy_context() 



