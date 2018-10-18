import discord
import asyncio
import EmojiDictionary


client = discord.Client()

@client.event
async def on_message(message):


    # we don't want bot replying to itself.
    if message.author == client.user:
        return


    # Replace inappropriate message with altered message.
    _author = message.author
    if str(_author)=='The_Jihad_Spot#1475':
        _content = "I'm gay"
    else:
        _content = message.content


    new_cont = ""
    # parse _content
    cont_words = str(_content).split(" ")
    # look for words in dictionary and replace them
    for word in cont_words:
        emoji = EmojiDictionary.emojiInterpreter(word)
        if emoji != None:
            word = emoji
        new_cont+=word+" "

    # concatenate new message
    newmsg=str(_author)+' says: '+str(new_cont)

    await client.delete_message(message) 
    await client.send_message(message.channel, newmsg)
    ########################################################


    # command list
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('!showmsg'):
        await client.wait_until_ready()
        async for msg in client.logs_from(cs_general_channel):
            print(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')

client.run('NTAyMzU2ODcwNTczMzI2MzM3.Dqm-Ig.LvLfGlq3n_1KvlFAroW5h_8K32Q')