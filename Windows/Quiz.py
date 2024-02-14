import dearpygui.dearpygui as pygui
from deep_translator import GoogleTranslator
import Windows.QuizLogic.Generate_Word as Generate_Word

current_window = None
incorrect_window = None
high_score = 0

def Start():
    global current_window
    if current_window:
        pygui.delete_item(current_window)
    generate_word = Generate_Word.Generate_Word()
    with pygui.window(label="Quiz", tag="Quiz", width=1200, height=1000, on_close=Exit):
        pygui.add_text("German Quizzr", parent="Quiz")
        pygui.add_text(generate_word, parent="Quiz", tag="word_text")
        pygui.add_text("What is the English translation?", parent="Quiz")
        pygui.add_input_text(label="Answer", parent="Quiz", tag="answer_input")
        pygui.add_button(label="Submit", callback=Submit, parent="Quiz")
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
        with pygui.window(label="Incorrect", width=600, height=200, on_close=Menu_Exit):
            if answer.lower() == english_translation.lower():
                high_score += 1
                Exit()
                Start()
            else:
                pygui.add_text(f"Incorrect: Correct answer: {english_translation}", parent="Incorrect")
                pygui.add_text(f"Your score: {high_score}", parent="Incorrect")
                incorrect_window = "Incorrect"
 
        pygui.set_value("answer_input", "")  # Clear the input field
    else:
        pygui.add_text("No Internet Connection..", parent="Quiz")

def Exit():
    global current_window
    global incorrect_window
    global high_score
    pygui.delete_item(current_window)
    try:
        current_window = "Exit_Screen_Game"
        with pygui.window(label="Exit_Screen_Game", width=600, height=200, on_close=Menu_Exit):
            pygui.add_text(f"Your score: {high_score}", parent="Exit_Screen_Game")
        
    except:
        pass

    pygui.delete_item(current_window)
    current_window = None

def Menu_Exit():
    global incorrect_window
    pygui.delete_item(incorrect_window)
    incorrect_window = None
        

