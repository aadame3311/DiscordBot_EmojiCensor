d = dict(shit=':poop:',
         shet=':poop:',  
         shity=':poop:',
         fuck=':dolphin:',
         fucking=':dolphin:',
         fuk=':dolphin:',
         fuc=':dolphin:')

def emojiInterpreter(word):
    if word in d:
        return d[word]
    else:
        return None