emoji_dict = dict(shit=':poop:',
        shet=':poop:',  
        fuck=':dolphin:',
        fukc=':dolphin:',
        fack=':dolphin:',
        fock=':dolphin:',
        fak=':dolphin:',
        fuk=':dolphin:',
        fuc=':dolphin:',
        ashole=':peach:',
        bitch=':dog:',
        niger=':grinning:',
        fag=':lipstick:'
    
         
         
         
         )

def emojiInterpreter(word):
    if word in emoji_dict:
        return emoji_dict[word]
    else:
        return None