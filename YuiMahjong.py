import discord
import os
import numpy as np


MAHJONG_ASCII = [n for n in range(48,58)] + [115, 112, 109, 122]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Initiallizing the Latex file

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author != client.user:
        print(message.author, message.content)

        if 'oppai' in message.content:
            print("sent")
            await message.channel.send('BOOBs')

        if 'yui' in message.content:
            print("sent")
            await message.channel.send('<:lilyO:1009861944150343770>')

        if message.content.startswith('mahjong'):

            tiles = message.content[8:]
            if np.all([ord(s) in MAHJONG_ASCII for s in tiles]):
                with open('LaTeX/Mahjong.tex','w') as file:
                    file.write(r'\documentclass{standalone}'+'\n')
                    file.write(r'\usepackage{tikz}'+'\n')
                    file.write(r'\usepackage{mahjong}'+'\n\n')

                    file.write(r'\begin{document}'+'\n')
                    file.write(r'\begin{tikzpicture}'+'\n')
                    file.write(r'\draw (0,0) node {\mahjong[%s]{%s}};'%('3cm',tiles)+'\n')
                    file.write(r'\end{tikzpicture}'+'\n')
                    file.write(r'\end{document}')

                os.system('"/Users/suzutsuki-ch/bin/xelatex" -interaction=nonstopmode LaTeX/Mahjong.tex')
                os.system('convert -density 300 Mahjong.pdf -quality 110 LaTeX/Tiles/temp.png')
                await message.channel.send(file = discord.File('LaTeX/Tiles/temp.png'))
                os.remove('LaTeX/Tiles/temp.png')
                os.remove('Mahjong.pdf')
                os.remove('Mahjong.log')
                os.remove('Mahjong.aux')

    
    # your code to process the message goes here

client.run('MTA4OTk1NzI4MjE3MjkxMTY2Nw.GTTVwr.GZJOVcSLEqCVhWEqUL8mKQVSHxTlGdN87KeICY')

