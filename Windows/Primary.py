import sys
import dearpygui.dearpygui as pygui
import Windows.Quiz as quiz
import Settings.Fonts as fonts

sys.path.append('../Settings/')
import Settings.Score_Saver as Score_Saver
# Primary Window

def Start():
    high_score = Score_Saver.Get_Score()
    with pygui.window(label="Primary Window", tag="Primary Window", width=1000, height=1000, on_close=Menu_Exit):
        pygui.add_text("German Quizzr", parent="Primary Window")
        pygui.add_button(label="Start Quiz", callback=Start_Quiz, parent="Primary Window")
        pygui.add_text(f"High Score: {high_score}", parent="Primary Window")

def Start_Quiz():
    quiz.Start()

def Menu_Exit():
    pygui.destroy_context() 


