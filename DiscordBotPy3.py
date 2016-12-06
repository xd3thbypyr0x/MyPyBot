import discord
import asyncio
import codecs
import urllib.request
import urbandict
import json
import discord.opus

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    #print(message.author, message.content, message.channel.id)
    #^^^ For debug reasons
    if message.content.startswith('!test'):
        await client.send_message(message.channel, "Pls no spam")

    elif message.content.startswith('!joinvoice'):
        await client.join_voice_channel(client.get_channel("255437555212877824"))
        opus = discord.opus
        opus.load_opus("opus")

    elif message.content.startswith('!leavevoice'):
        voice = discord.VoiceClient
        voice.disconnect("250169864000503808")

    elif message.content.startswith('!fury'):
        await client.send_message(message.channel, "ITS THE FURY")
        await asyncio.sleep(1)
        await client.send_message(message.channel, "OF")
        await asyncio.sleep(1)
        await client.send_message(message.channel, "THE")
        await asyncio.sleep(3)
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=5i7qZxICwgQ")
        await client.send_message(message.channel, "STOMROMROSMROMRORMOMROMORMOMSMRO")

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, "The available commands are, !test, !fury, !help, !sleep, !shutdown (owner only), !urban")

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith("!shutdown") and message.author.id == "172979233260437505":
        await client.send_message(message.channel, "Goodbye! :vulcan:")
        await client.close()
        #await exit()

    elif message.content.startswith('!urban'):
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

        await client.send_message(message.channel, "{} {} {} {}" .format(search, "|", "Definition:", definition))
        #await client.send_message(message.channel, "{} {}" .format("Definition:", definition))

    else:
        if message.content.startswith('!'):
            await client.send_message(message.channel, "This command doesn't exist / you're not allowed to use it. Fuck off.")

client.run('ejensenmet@gmail.com', 'rawrrawr')
