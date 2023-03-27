import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


async def on_ready():
    print(f'{client.user} has connected to Discord!')


async def on_message(message):
    if message.author == client.user:
        return 0
    
    # your code to process the message goes here

client.run('MTA4OTk1NzI4MjE3MjkxMTY2Nw.GTTVwr.GZJOVcSLEqCVhWEqUL8mKQVSHxTlGdN87KeICY')