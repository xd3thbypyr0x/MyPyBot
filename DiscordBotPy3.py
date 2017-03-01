import discord
import asyncio
import codecs
#import yolodb
import urllib.request
import urbandict
import youtube_dl
import json
import discord.opus
from ctypes.util import find_library
import opuslib
#import botpassword
#this is a local file with my token
import logging
#from opus_loader import load_opus_lib
#load_opus_lib()

"""async def joinVoiceChannel():
t
    channel = client.get_channel("222841882131038215")
    client.join_voice_channel(channel)
    print('Bot should joined the Channel')"""
    #SHIT THAT AINT WORKING

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()
#voice = discord.VoiceClient()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #await joinVoiceChannel()
    #find_library("opus")

@client.event
async def on_message(message):
    #print(message.author, message.content, message.channel.id)
    #^^^ For debug reasons
    owner = "172979233260437505"
    if message.content.startswith('?test') and message.author.id == (owner):
        await client.send_message(message.channel, "Pls no spam")

    #elif message.author.id == "255363303369474059":
        #await client.send_message(message.channel, "fuk off")

    elif message.content.startswith("?whitelist"):
        words = message.content.split()
        print(words)
        del words[0]
        owner = owner + words
        print(owner[0])

    elif message.content.startswith('?fury') and message.author.id == "172979233260437505":
        await client.send_message(message.channel, "ITS THE FURY")
        await asyncio.sleep(1)
        await client.send_message(message.channel, "OF")
        await asyncio.sleep(1)
        await client.send_message(message.channel, "THE")
        await asyncio.sleep(3)
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=5i7qZxICwgQ")
        await client.send_message(message.channel, "STOMROMROSMROMRORMOMROMORMOMSMRO")

    elif message.content.startswith('?help'):
        await client.send_message(message.channel, "The available commands are, ?test, ?fury, ?help, ?sleep, ?shutdown (owner only), ?urban")

    elif message.content.startswith('?sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    #elif message.author.id == "117049583036530694":
        #await client.send_message(message.channel, "Shut up you're 12")

    elif message.content.startswith("?shutdown") and message.author.id == "172979233260437505":
        await client.send_message(message.channel, "Bye Cunt")
        await client.close()
        #await exit()

    elif message.content.startswith("?check"):
        if discord.opus.is_loaded() == True:
            await client.send_message(message.channel, "Opus is loaded")
        elif discord.opus.is_loaded() == False:
            await client.send_message(message.channel, "Opus is not loaded")

    elif message.content.startswith("?join"):
        roomid = message.content.split()
        del roomid [0]
        newroomid = roomid[0]
        channel = client.get_channel(newroomid)
        print(channel)
        await client.join_voice_channel(channel)
        discord.opus.load_opus("opus")

    elif message.content.startswith("?tesaudio"):
        channel = client.get_channel("255437555212877824")
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=7qFF2v8VsaA')
        player.start()

    elif message.content.startswith("?play") and message.author.id == "172979233260437505":
        #discord.opus.is_loaded() == True:
        """url = message.content.split()
        del url[0]
        urlnew = url[0]
        print(urlnew)"""
        player = await discord.VoiceClient.create_ytdl_player('http://www.youtube.com/watch?v=7qFF2v8VsaA')
        player.volume = "0.5"
        player.start()

        """url = message.content.split()
        del url[0]
        urlnew = url[0]
        print("This the link boyo" + " " + urlnew)
        #channel = client.get_channel("222841882131038215")
        #voice = await client.join_voice_channel(channel)
        player = await discord.VoiceClient.create_ytdl_player(urlnew)

        #del urlnew[0]
        player.volume = 0.1
        player.start()"""

    elif message.content.startswith("?pause"):
            discord.VoiceClient.StreamPlayer.pause()

    elif message.content.startswith("?leave"):
        await discord.VoiceClient.disconnect("self")

    elif message.content.startswith("?ss") and message.author.id == "172979233260437505":
        await client.close()

    elif message.content.startswith("Would Ethan eat ass?"):
        await client.send_message(message.channel, "Goddamn Right he would")

    #elif message.content.startswith("?status"):
    #    Game = message.content.split()
    #    del Game[0]
    #    print(Game)
    #    client.change_status(game=Game, idle =False)
#LEARN TO READ SHIT BOI

    elif message.content.startswith('?urban'):
        words = message.content.split()
        del words[0]
        search = ""
        for word in words:
            search = search + word + " "

        url = 'http://api.urbandictionary.com/v0/define?term=%s' % (search)

        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(response))
        definition = data['list'][0]['definition']
        search = search.title()

        await client.send_message(message.channel, search)
        await client.send_message(message.channel, "-------------")
        await client.send_message(message.channel, definition)
        #await client.send_message(message.channel, "{} {}" .format("Definition:", definition))

    else:
        """"if message.content.startswith('?'):
            await client.send_message(message.channel, "This command doesn't exist / you're not allowed to use it. Fuck off.")
"""
#Mass commented out ^^^
client.run(#credentials)
