@commands.has_permissions(adminictrator=True)

@client.event
async def on_member_join(member):
    channel = client.get_channel(878378482218962975)
    print("hi")
    role = discord.utils.get(member.guild.roles, id=879143307077374052)
    await member.add_roles(role)