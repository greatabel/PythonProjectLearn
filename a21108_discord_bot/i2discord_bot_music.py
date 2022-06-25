import sys
import codecs


# import certifi
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("中文")

import discord
import os 

import urllib.request
import re

import json

'''
第一个，当用户输入!play 音乐名，就会从youtube里找音乐来放歌，再或者!play 网站链接 来放这个链接里的音频。 

第二个，用户输入!用户名字 输出我对他的评价，比如!flukun, bot就会输出我对这个人的评价
还有放音乐的功能，输入!skip就是跳过当曲

第三个功能就是我进行录音，比如输出!shittalk1 就会输出我在这里面录的内容，!shittalk2就会输出那里面的内容

'''

# -----start 读取json文件
f = open('evaluation_on_people.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  

for i in data['evaluations']:
    print(i)
  

f.close()
for i in data['evaluations']:
    print(i, '#')
# -----end  读取json文件


def get_youtube_url(search_keyword):
    # search_keyword="mozart"
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])
    return "https://www.youtube.com/watch?v=" + video_ids[0]


token = ''
token = os.environ['token']
print('i2')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello from J-Lambo-bot Echo!')

    if message.content.startswith('!play'):
        keyword = message.content.replace("!play ", "")
        r = get_youtube_url(keyword)
  
        # r = 'https://www.youtube.com/watch?v=5XK2C9w6oVk&list=PLTomFrxjhvMzQEGfD8xSUp_S7mqDsJLku'
        await message.channel.send('!play ' + r)
    # handle comments
    if message.content.startswith('!'):
        r = None
        for i in data['evaluations']:
            if message.content == '!'+i['name']:
                r = i['comment']
        await message.channel.send(r)
print("os.getenv('TOKEN')=", token)
client.run(token)
