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
    act = discord.Activity(type = discord.ActivityType.listening, name = "!spoede")
    await client.change_presence(activity = act)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "!spoede":
        print(f"Recieved request from {str(message.author)} in channel {str(message.channel)}")
        out = spoede.spoede()
        print(f"Responding: {out}")
        await message.channel.send(out)

client.run(TOKEN)