import discord
import asyncio
import EmojiDictionary
import EmojiCensorCommands
import re


client = discord.Client()
class MESSAGE:
    def __init__(self):
        self.message = ""
        self.author = ""
        self.message_altered = False



# some pre set variables.
newmsg = ""
def replace_words(_author, _message):
    message = MESSAGE()
    message.message = _message
    message.author = _author
    message.message_altered = False

    new_cont=""
    cont_words = re.split('\s|[0-9]', str(message.message))
    # look for words in dictionary and replace them
    for word in cont_words:
        # we don't want to take words with repeated letters into account...
        # as this could create an infinite number of ways a word could be written.
        tmp_word = re.sub(r'(.)\1+',r'\1', word)
        # check if the string contains an inappropriate word as a substring.
        for bad_word in EmojiDictionary.emoji_dict:
            if bad_word in tmp_word:
                tmp_word = bad_word
                break
        # use dictionary to find emoji equivalent of our word.
        emoji = EmojiDictionary.emojiInterpreter(tmp_word)
        if emoji != None:
            word = emoji
            message.message_altered = True

        #construct new message content.
        new_cont+=word+" "
        # concatenate new message content with the author.
        message.message=str(message.author)+' says: '+str(new_cont)
        
    return message


#EVENTS.
@client.event
async def on_message(message):

    # some commands can only be run by server admins.
    ADMIN = message.author.server_permissions.administrator

    
    # we don't want bot replying to itself.
    if message.author == client.user:
        return

    # Replace inappropriate message with altered message.
    _author = message.author
    _content = message.content


    # will only replace text if an inappropriate word was found.
    new_message = replace_words(_author, _content)
    if new_message.message_altered:
        await client.delete_message(message) 
        await client.send_message(message.channel, new_message.message)
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

# not actual token.
client.run(token)