import discord
import os 

'''
第一个，当用户输入!play 音乐名，就会从youtube里找音乐来放歌，再或者!play 网站链接 来放这个链接里的音频。 

第二个，用户输入!用户名字 输出我对他的评价，比如!flukun, bot就会输出我对这个人的评价
还有放音乐的功能，输入!skip就是跳过当曲

第三个功能就是我进行录音，比如输出!shittalk1 就会输出我在这里面录的内容，!shittalk2就会输出那里面的内容

'''

token = ''
token = os.environ['token']

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
