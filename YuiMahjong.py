import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author != client.user:
        print(message.content)
    
        if 'oppai' in message.content:
            print("sent")
            await message.channel.send('BOOBs')

        if message.content.startswith('yui'):
            print("sent")
            await message.channel.send('<:lilyO:1009861944150343770>')
    
    # your code to process the message goes here

client.run('MTA4OTk1NzI4MjE3MjkxMTY2Nw.GTTVwr.GZJOVcSLEqCVhWEqUL8mKQVSHxTlGdN87KeICY')