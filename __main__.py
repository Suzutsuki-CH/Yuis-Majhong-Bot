import discord
import os
import numpy as np
from YuiAux import *

from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.meld import Meld
from mahjong.shanten import Shanten


# Possible ASCII codes of characters in a mahjong string
MAHJONG_ASCII = [n for n in range(48,58)] + [115, 112, 109, 122]

# Calculating Shanten/向聽
shanten = Shanten()

# Necessary setting for discord bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# When yui is connected notify
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Reponse to messages
@client.event
async def on_message(message):
    sent = False
    if message.author != client.user:
        print(message.author, message.content)


        if np.random.randint(6) == 0:
            await message.channel.send(np.random.choice(['<:yuiNotme:1009859812441456670>',
                                        '<:yuiOVO:1009859221313040435>', 
                                        '<:yuilovelove:1010149916728885259>',
                                        '<:yuithumbdown:1009859498346807317>',
                                        '<:yuiO:1009859418965422150>',
                                        '<:yuiStink:1009859639929749504>']))
            print("sent")
            sent = True


        # React to any message with 'oppai'
        if 'oppai' in message.content and not sent:
            print("sent")
            await message.channel.send('BOOBs')
            sent = True

        # React to any message with 'yui'
        if 'yui' in message.content and np.random.randint(2)==1 and not sent:
            await message.channel.send(np.random.choice(['<:yuiNotme:1009859812441456670>',
                                        '<:yuiOVO:1009859221313040435>', 
                                        '<:yuilovelove:1010149916728885259>',
                                        '<:yuithumbdown:1009859498346807317>',
                                        '<:yuiO:1009859418965422150>',
                                        '<:yuiStink:1009859639929749504>']))
            print("sent")
            sent = True


        # Calculating Shanten, Han, and Fu
        if message.content.startswith("$suan"):
            t = message.content[6:]
            if np.all([ord(s) in MAHJONG_ASCII for s in t]):
                TenhouArr = TenhouGenerate(t)
                tiles = TilesConverter.string_to_34_array(man=TenhouArr[0], sou=TenhouArr[1], pin=TenhouArr[2], honors=TenhouArr[3])
                result = shanten.calculate_shanten(tiles)
                numTiles = np.sum([len(TenhouArr[i]) for i in range(0,4)])
                print(numTiles)

                if result == 0 and numTiles == 14:
                    await message.channel.send(f"小唯聽牌了！")
                    LaTeX_Generate(t)
                    await message.channel.send(file = discord.File('LaTeX/Tiles/temp.png'))
                    sent = True
                elif result == -1 and numTiles == 14:
                    await message.channel.send(f"小唯和了！")
                    LaTeX_Generate(t)
                    await message.channel.send(file = discord.File('LaTeX/Tiles/temp.png'))
                    sent = True
                elif numTiles == 14:
                    await message.channel.send(f"小唯再摸{result}張牌就可以聽牌了！")
                    LaTeX_Generate(t)
                    await message.channel.send(file = discord.File('LaTeX/Tiles/temp.png'))
                    sent = True
                elif numTiles > 14:
                    await message.channel.send(f"小唯手上牌有點多！")
                elif numTiles < 14:
                    await message.channel.send(f"誰偷走了小唯的牌？")

            if sent: CleanUp()

        # Generate Mahjong Tiles
        if message.content.startswith('$mahjong'):

            tiles = message.content[9:]
            if np.all([ord(s) in MAHJONG_ASCII for s in tiles]):
                LaTeX_Generate(tiles)
                await message.channel.send(file = discord.File('LaTeX/Tiles/temp.png'))
                CleanUp()

    
    # your code to process the message goes here

client.run('MTA4OTk1NzI4MjE3MjkxMTY2Nw.GTTVwr.GZJOVcSLEqCVhWEqUL8mKQVSHxTlGdN87KeICY')

