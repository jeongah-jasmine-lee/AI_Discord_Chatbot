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

# Keep track of the current game state
game_active = False
scoreboard = {}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Check if the game is on
    if game_active:
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
    random.shuffle(multi_choice_qas)
    for idx, multi_choice_qa in enumerate(multi_choice_qas):
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

        if idx == len(multi_choice_qas) - 1:
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

# Command to start the game
@client.command(name="startgame")
async def start_game(ctx):
    global game_active
    global scoreboard
    if game_active:
        await ctx.send("A game is already in progress!")
        return
    
    game_active = True
    scoreboard = {}  # Reset the scoreboard
    rounds = 5  # Number of rounds in the game
    await ctx.send("Game is on! Get ready for some multiple-choice questions!")

    random.shuffle(multi_choice_qas)
    for round in range(rounds):
        multi_choice_qa = multi_choice_qas[round]
        qa_text = f"**{multi_choice_qa['question']}**\n" + "\n".join(multi_choice_qa['choices'])
        await ctx.send(f"Round {round+1} / {rounds}: {qa_text}")

        # Check for the user's response
        def check(msg):
            return msg.channel == ctx.channel and msg.author != client.user  # Exclude bot's own messages

        try:
            msg = await client.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            await ctx.send(f'Time\'s up! The correct answer was **{multi_choice_qa["correct"]}**.')
        else:
            # Check if the selected answer is correct
            # TODO: check rules
            if multi_choice_qa["correct"].lower() in msg.content.lower()[:2]:
                winner = msg.author
                if winner not in scoreboard:
                    scoreboard[winner] = 0
                scoreboard[winner] += 1
                await ctx.send(f'Correct! {winner.mention} scores a point!')
            else:
                await ctx.send(f'Wrong! The correct answer was **{multi_choice_qa["correct"]}**.')

    game_active = False
    await display_scoreboard(ctx)

# Display the scoreboard
async def display_scoreboard(ctx):
    if scoreboard:
        sorted_scores = sorted(scoreboard.items(), key=lambda item: item[1], reverse=True)
        
        # Construct the scoreboard UI with headers and rows
        score_message = "🏆 ***Final Scores*** 🏆\n"
        score_message += "---------------------------------\n"
        score_message += "{:<20} | {:>6}\n".format("Player", "Points")
        score_message += "---------------------------------\n"
        
        for user, score in sorted_scores:
            score_message += "{:<20} | {:>6}\n".format(user.name, score)
        
        score_message += "---------------------------------\n"

        await ctx.send(f"```{score_message}```")  # Display the scoreboard in a code block for better alignment
    else:
        await ctx.send("No one scored any points. Better luck next time!")

# Start the bot
client.run(DISCORD_TOKEN)