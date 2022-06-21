import discord

token = ''
# token = 'OTg1ODQ3OTAzNTk3NzgxMDky.GX0Tl-.xmOvshdgfxfCtYWGG4nAQgrn71xtSvuHx0_D5A'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


print("os.getenv('TOKEN')=", token)
client.run(token)
