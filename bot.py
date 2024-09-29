import os
import discord
from dotenv import load_dotenv
from chatgpt import send_to_chatGpt

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    messages = [{"role": "user", "content": message.content}]
    response = send_to_chatGpt(messages)
    await message.channel.send(response)


# Start the bot
client.run(DISCORD_TOKEN)