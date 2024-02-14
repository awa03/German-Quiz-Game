
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
high_score_file = os.path.join(script_dir, '..', 'Settings', 'Saved_Data', 'High_Score.txt')

def Save_Score(score):
    if os.path.exists(high_score_file) and os.path.getsize(high_score_file) > 0:
        with open(high_score_file, "r") as file:
            content = file.read().strip()
            if content.isdigit():
                current_high_score = int(content)
            else:
                current_high_score = 0  # Set default high score if content is not numeric
    else:
        current_high_score = 0  # Set default high score if file does not exist or is empty

    if score > current_high_score:
        with open(high_score_file, "w") as file:
            file.write(str(score))
        return True
    return False


def Get_Score():
    if os.path.exists(high_score_file) and os.path.getsize(high_score_file) > 0:
        with open(high_score_file, "r") as file:
            content = file.read().strip()
            if content.isdigit():
                return int(content)
    return 0




