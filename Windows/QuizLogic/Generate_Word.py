import zufallsworte as zufall

def Generate_Word():
    words = zufall.zufallswoerter(1)
    return words[0] if words else None



