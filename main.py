import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    print('BOT_connected')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="registration")
    no_name = discord.utils.get(member.guild.roles, name='no_name')
    await member.add_roles(no_name)
    await channel.send(f'{member.mention} .reg чтобы зарегистрироваться (Фамилия Имя Номер_группы)')


@client.event
async def on_message(msg):
    channel_meme = discord.utils.get(msg.guild.text_channels, name="memes")
    channel_rofl = discord.utils.get(msg.guild.text_channels, name="rofls")
    if (msg.channel == channel_meme) | (msg.channel == channel_rofl):
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
    await client.process_commands(msg)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await ctx.send(f'ban user {member.mention}')


@client.command(pass_context=True)
async def help(ctx):
    emb = discord.Embed(title='Навигация по командам')
    emb.add_field(name='{}reg'.format("."), value='Регистрация')
    emb.add_field(name='{}roll [n]'.format("."), value='Случайное число в диапазоне 1-n')
    await ctx.send(embed=emb)


@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='mute')
    await member.add_roles(mute_role)


@client.command()
async def roll(ctx, num):
    if num.isdigit():
        print('a')
        await ctx.send(f'{ctx.author.mention} получает случайное число(1-{num}): {random.randint(1, int(num))}')


@client.command()
async def reg(ctx, surname=' ', name=' ', group=' '):
    channel = discord.utils.get(ctx.guild.text_channels, name="registration")
    if ctx.channel != channel:
        msg = await channel.fetch_message(ctx.message.id)
        await msg.delete()
    if (not group.isdigit()) | (surname == ' ') | (name == ' ') | (group == ' '):
        await ctx.send(f'{ctx.author.mention}, введите ".reg Фамилия Имя №Группы" для регистрации.')
    else:
        student = discord.utils.get(ctx.message.guild.roles, name='student')
        await ctx.author.edit(nick='{0} {1}'.format(surname, name))
        no_name = discord.utils.get(ctx.message.guild.roles, name='no_name')
        await ctx.author.remove_roles(no_name)
        if group[0] == '0':
            not_student = discord.utils.get(ctx.message.guild.roles, name='not-student')
            await ctx.author.add_roles(not_student)
        if group[0] == '1':
            await ctx.author.add_roles(student)
            k1 = discord.utils.get(ctx.message.guild.roles, name='1 курс')
            await ctx.author.add_roles(k1)
        elif group[0] == '2':
            await ctx.author.add_roles(student)
            k2 = discord.utils.get(ctx.message.guild.roles, name='2 курс')
            await ctx.author.add_roles(k2)
        elif group[0] == '3':
            await ctx.author.add_roles(student)
            k3 = discord.utils.get(ctx.message.guild.roles, name='3 курс')
            await ctx.author.add_roles(k3)
        elif group[0] == '4':
            await ctx.author.add_roles(student)
            k4 = discord.utils.get(ctx.message.guild.roles, name='4 курс')
            await ctx.author.add_roles(k4)

    # if group.isdigit():
    # добавить роль, обозначающую группу

token = open('token.txt').readline()
client.run(token)
