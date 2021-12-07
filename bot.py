# bot.py
import os
import random
import discord
from dotenv import load_dotenv
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')
    
    print(guild.channels)
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # @everyone 
    msg = "Dead disc <:sadge:791845070709719102> <:sippin:746435843127771266> "
    timeout = time.time() + 60*5  # 2 hours 60*120
 
    while time.time() < timeout:
        continue
        
    print("time to roll")
    return await message.channel.send(msg)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '$phrase':
        lines = open('random-phrase.txt').read().splitlines()
        myline = random.choice(lines)
        return await message.channel.send(myline)
        
client.run(TOKEN)
