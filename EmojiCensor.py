import discord
import asyncio
import EmojiDictionary
import re


client = discord.Client()

# some pre set variables.




#EVENTS.
@client.event
async def on_message(message):
    if message.author == "ChickenBoy956#8947":
        await client.send_message(message.channel, '{0.message.author} is big gay!'.format(message))



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


    # command list
    if message.content.startswith('!hello'):

        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    elif message.content.startswith('!showmsg'):
        await client.wait_until_ready()
        async for msg in client.logs_from(cs_general_channel):
            print(msg)
    
    elif message.content.startswith('!help'):
        em = discord.Embed(title='Emoji Censor Info', description='EmojiCensor will censor out any inappropriate language with an emoji.', colour=0xDEADBF)
        await client.send_message(message.channel, embed=em)

    if message.content.startswith('!delete-msg') and ADMIN:
        # init list of messages to be deleted
        msgs=[]
        async for x in client.logs_from(message.channel):
            msgs.append(x)
        
        # get confirmation from user.
        await client.send_message(message.channel, 'Are you sure you want to delete the past {} messages in this channel? (y/n)'.format(len(msgs)))

        # wait for user to response with 'y'...
        # if user replies with anything else, it does nothing.
        response = await client.wait_for_message(author=message.author, content='y')
        await client.send_message(message.channel, 'Deleting messages...')

        # store past 100 messages into the messages list (discord only allows 100 messages to be deleted at a time)

        await client.delete_messages(msgs)
    elif ADMIN == False:
        await client.send_message(message.channel, '{0.author.mention} Must be an administrator to use this command'.format(message))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')

client.run('NTAyMzU2ODcwNTczMzI2MzM3.Dqm-Ig.LvLfGlq3n_1KvlFAroW5h_8K32Q')