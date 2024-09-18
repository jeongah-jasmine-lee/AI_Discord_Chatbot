import os
import discord

# Directly assign the token (replace 'YOUR_DISCORD_TOKEN' with your actual token)
TOKEN = #fill your token

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith("Hello"):
        await message.channel.send("Hi, Nice to meet you. I am OS Bot")
# start the bot
client.run(TOKEN)
