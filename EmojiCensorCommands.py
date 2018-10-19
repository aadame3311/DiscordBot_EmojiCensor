import discord

# command list
async def command(ADMIN, client, message):
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