emoji_dict = dict(shit = ':poop:',
        shet = ':poop:',  
        fuck = ':dolphin:',
        fukc = ':dolphin:',
        fack = ':dolphin:',
        fock = ':dolphin:',
        fak = ':dolphin:',
        fuk = ':dolphin:',
        fuc = ':dolphin:',
        fuq = ':dolphin:',
        ashole = ':peach:',
        bitch = ':dog:',
        niger = ':no_entry_sign:',
        fag = ':no_entry_sign:',
        dick = ':bird:',
        pusy = ':cat:',
        slut = ':no_entry_sign:',
        whore = ':no_entry_sign:',
        cunt = ':no_entry_sign:',
        skank = ':no_entry_sign:',
        bastard = ':no_entry_sign:',
        choad = ':bird:',
        biatch = ':dog:',
        dyke = ':no_entry_sign:',
        cock = ':bird:',
        quer = ':no_entry_sign:',
        homo = ':no_entry_sign:'
         )

def emojiInterpreter(word):
    if word in emoji_dict:
        return emoji_dict[word]
    else:
        return None