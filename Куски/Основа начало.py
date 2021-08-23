import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('BOT_connected')

token = open('token.txt').readline()
client.run(token)