import sys
import dearpygui.dearpygui as pygui
from deep_translator import GoogleTranslator
import Windows.QuizLogic.Generate_Word as Generate_Word

sys.path.append('../Settings/')
import Settings.Score_Saver as Score_Saver

current_window = None
incorrect_window = None
high_score = 0

def Start():
    global current_window
    if current_window:
        pygui.delete_item(current_window)
    generate_word = Generate_Word.Generate_Word()
    with pygui.window(label="Quiz",
                      tag="Quiz",
                      width=1500,
                      height=1000,
                      on_close=Exit,
                      no_resize=True,
                      no_collapse=True,
                      no_scrollbar=True,
                      no_move=True,
                      no_title_bar=True,
                      pos=(0,0),
                      ):
        pygui.add_text("German Quizzr", parent="Quiz")
        pygui.add_text(generate_word, parent="Quiz", tag="word_text")
        pygui.add_text("What is the English translation?", parent="Quiz")
        pygui.add_input_text(parent="Quiz", tag="answer_input",
                             width=1265, height=100,
                             )
        pygui.add_button(label="Submit", callback=Submit, parent="Quiz"
                         , width = 1265, height=100
                         )
        pygui.add_button(label="x", callback=Exit, parent="Quiz"
                            , width = 1265, height=40)
    current_window = "Quiz"

def translate_to_english(german_word):
    translation = GoogleTranslator(source='de', target='en').translate(german_word)
    return (translation)

def Submit(sender, data):
    global incorrect_window
    global high_score
    answer = pygui.get_value("answer_input")
    generate_word = pygui.get_value("word_text")
    english_translation = translate_to_english(generate_word)
    print(english_translation)
    print(answer)
    if english_translation is not None:
        with pygui.window(label="Incorrect",
                          tag="Incorrect",
                          width=600, height=200,
                          no_resize=True,
                          no_collapse=True,
                          no_scroll_with_mouse=True,
                          no_title_bar=True,
                          no_close=True,
                          no_move=True,
                          no_background=True,
                          pos=(400, 400)
                          ):
            if answer.lower() == english_translation.lower():
                high_score += 1
                Score_Saver.Save_Score(high_score)
                Exit()
                Start()
            else:
                pygui.add_text(f"Incorrect: Correct answer: {english_translation}", parent="Incorrect")
                pygui.add_text(f"Your score: {high_score}", parent="Incorrect")
                pygui.add_button(label="Override, I got this right", callback=Override, parent="Incorrect")
                pygui.add_button(label="Exit", callback=Menu_Exit, parent="Incorrect")
                incorrect_window = "Incorrect"
 
        pygui.set_value("answer_input", "")  # Clear the input field
    else:
        pygui.add_text("No Internet Connection..", parent="Quiz")

def Exit():
    global current_window
    global incorrect_window
    global high_score

    pygui.delete_item(current_window, children_only=True)
    pygui.delete_item(current_window)
    pygui.delete_item(incorrect_window)
    current_window = None
    incorrect_window = None
    try:
        incorrect_window = "Exit_Screen_Game"
        with pygui.window(label="Exit_Screen_Game",
                        tag="Exit_Screen_Game",
                          width=490,
                          height=70,
                          on_close=Menu_Exit,
                          no_resize=True,
                          no_collapse=True,
                          no_scrollbar=True,
                          no_move=True,
                          no_title_bar=True,
                          pos=(775, 40),
                          ):
            pygui.add_text(f"Your score: {high_score}", parent="Exit_Screen_Game")
            pygui.add_button(label="Exit", callback=Exit_Screen, parent="Exit_Screen_Game")
        
    except:
        pass

def Exit_Screen(sender, data):
    pygui.delete_item("Exit_Screen_Game")

def Menu_Exit():
    global incorrect_window
    pygui.delete_item(incorrect_window)
    incorrect_window = None
        
def Override(sender, data):
    global high_score
    global incorrect_window
    pygui.delete_item(incorrect_window)
    high_score += 1
    Score_Saver.Save_Score(high_score)
    Exit()
    Start()
    
