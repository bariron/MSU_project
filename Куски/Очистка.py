@client.command(pass_context=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
