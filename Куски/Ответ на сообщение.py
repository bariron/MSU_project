@client.command( pass_context = True)
async def hello (ctx):
    author = ctx.message.author
    await ctx.send(f'{author.mention} hello')
