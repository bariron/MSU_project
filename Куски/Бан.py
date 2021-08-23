@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await ctx.send(f'ban user {member.mention}')
