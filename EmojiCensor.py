import discord


client = discord.Client()

@client.event
async def on_message(message):
    # we don't want bot replying to itself.
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')

client.run('NTAyMzU2ODcwNTczMzI2MzM3.Dqm-Ig.LvLfGlq3n_1KvlFAroW5h_8K32Q')