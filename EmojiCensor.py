import discord
import asyncio
import EmojiDictionary
import EmojiCensorCommands
import re


client = discord.Client()

# some pre set variables.




#EVENTS.
@client.event
async def on_message(message):

    # some commands can only be run by server admins.
    ADMIN = message.author.server_permissions.administrator

    new_cont=""
    inappropriate = False
    
    # we don't want bot replying to itself.
    if message.author == client.user:
        return

    # Replace inappropriate message with altered message.
    _author = message.author
    _content = message.content
    # parse _content
    cont_words = re.split('\s|[0-9]', str(_content))
    # look for words in dictionary and replace them
    for word in cont_words:
        # we don't want to take words with repeated letters into account...
        # as this could create an infinite number of ways a word could be written.
        word = re.sub(r'(.)\1+',r'\1', word)
        # check if the string contains an inappropriate word as a substring.
        for bad_word in EmojiDictionary.emoji_dict:
            if bad_word in word:
                word = bad_word
                break
        # use dictionary to find emoji equivalent of our word.
        emoji = EmojiDictionary.emojiInterpreter(word)
        if emoji != None:
            word = emoji
            inappropriate = True
        new_cont+=word+" "


    # concatenate new message
    newmsg=str(_author)+' says: '+str(new_cont)

    # will only replace text if an inappropriate word was found.
    if inappropriate:
        await client.delete_message(message) 
        await client.send_message(message.channel, newmsg)
    ##############################################################
    # send command(message) data to the EmojiCensorCommands file for processing.
    await EmojiCensorCommands.command(ADMIN, client, message)
    ##############################################################

    

  


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')

client.run('NTAyMzU2ODcwNTczMzI2MzM3.Dqm-Ig.LvLfGlq3n_1KvlFAroW5h_8K32Q')