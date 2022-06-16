import discord
import os
import spoede
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents = discord.Intents.default())

@client.event
async def on_ready():
    print(f"{client.user} connected")
    act = discord.CustomActivity("!spoede")
    await client.change_presence(activity = act)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "!spoede":
        await message.channel.send(spoede.spoede())

client.run(TOKEN)