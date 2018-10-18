def emojientrepreture(switchit, word):
    if word in switchit.keys():
        value = switchit[word]
        return value
    else:
        return None


d = dict(shit=':poop:', fuck=':dolphin:')
word = input('Enter word: ')
print(emojientrepreture(d, word))