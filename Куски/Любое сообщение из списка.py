hello_words = ['hello', 'hi', 'привет']
@client.event
async def on_message(message):
    msg = message.content.lower()
    if msg in hello_words:
        await message.channel.send("CHO NADO?")