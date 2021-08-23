@client.event
async def on_ready():
    print('Succesfully logged in')
    await client.change_presence(activity=discord.Game(name="suck on " + str(len(client.guilds)) + ' server'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
      await message.channel.send("Hi Hitler")

async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))
