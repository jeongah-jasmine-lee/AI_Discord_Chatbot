import os
import asyncio
import discord
import random
from dotenv import load_dotenv
from chatgpt import send_to_chatGpt
from discord.ext import commands

from data import *

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
# client = discord.Client(command_prefix='!', intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Check if the message is a command
    ctx = await client.get_context(message)
    if ctx.command is not None:
        # Process command like !quiz
        await client.process_commands(message)
        return
    
    messages = [{"role": "user", "content": message.content}]
    response = send_to_chatGpt(messages)
    await message.channel.send(response)

# Command to start the quiz
@client.command(name="quiz")
async def quiz_command(ctx):
    random.shuffle(mutli_choice_qas)
    for idx, multi_choice_qa in enumerate(mutli_choice_qas):
        # Send the question and choices
        qa_text = f"**{multi_choice_qa['question']}**\n" + "\n".join(multi_choice_qa['choices'])
        question_message = await ctx.send(qa_text)
        
        # Add reaction emojis (A, B, C, D)
        reactions = {'🇦':'A', '🇧':'B', '🇨':'C', '🇩':'D'}
        for emoji in reactions: await question_message.add_reaction(emoji)
        
        # Wait for user's response
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in reactions
        
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'Time is up! The correct answer was **{multi_choice_qa["correct"]}**')
        else:
            # Check if the answer is correct
            if reactions[reaction.emoji] == multi_choice_qa["correct"]:
                await ctx.send("Correct!")
            else:
                await ctx.send(f'Wrong! The correct answer was **{multi_choice_qa["correct"]}**')

        if idx == len(mutli_choice_qas) - 1:
            finish_message = await ctx.send("Congrats! You have finished all questions.")
            break

        # Ask the user if they want to continue the quiz
        continue_message = await ctx.send("Do you want to continue to the next question? React with ✅ to continue or ❌ to stop.")
        
        # Add reaction emojis for continue (yes) and stop (no)
        await continue_message.add_reaction('✅')
        await continue_message.add_reaction('❌')
        
        # Check if user wants to continue or stop
        def continue_check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['✅', '❌']
        
        try:
            continue_reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=continue_check)
        except asyncio.TimeoutError:
            await ctx.send("Quiz ended. Thanks for playing!")
            break
        else:
            if continue_reaction.emoji == '❌':
                await ctx.send("Quiz ended. Thanks for playing!")
                break

# Start the bot
client.run(DISCORD_TOKEN)