d = dict(shit=':poop:',
         fuck=':dolphin:')

def emojiInterpreter(word):
    if word in d:
        return d[word]
    else:
        return None