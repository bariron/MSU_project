client.remove_command('help')
# Начало

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def help(ctx):
    emb = discord.Embed(title='Навигация по командам')

    emb.add_field(name='{}clear'.format("."), value='Очистка чата')

    await ctx.send(embed=emb)