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
                # await ctx.send("Correct!")
                await ctx.send(f"Correct!\n"
                               f'Explanation: {multi_choice_qa["explanation"]}\n'
                               f'Topic: **{multi_choice_qa["topic"]}**')
            else:
                # await ctx.send(f'Wrong! The correct answer was **{multi_choice_qa["correct"]}**')
                await ctx.send(f'Wrong! The correct answer was **{multi_choice_qa["correct"]}**.\n'
                               f'Explanation: {multi_choice_qa["explanation"]}\n'
                               f'Topic: **{multi_choice_qa["topic"]}**')

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


async def send_long_message(ctx, content):
    """Helper function to send messages that are longer than 2000 characters."""
    limit = 2000
    for i in range(0, len(content), limit):
        await ctx.send(content[i:i + limit])

@client.command(name="skillcheck")
async def skillcheck_command(ctx):
    global game_active
    if game_active:
        await ctx.send("A skill check is already in progress! 🚨")
        return

    game_active = True
    await ctx.send("🎓 **Welcome to the Skill Check!** 🎓\nHere are the available topics:")

    # List all topics
    topics_list = "\n".join([f"{key}: {value}" for key, value in topics.items()])
    await ctx.send(f"📚 Please choose a topic by typing the topic number (e.g., `1`):\n{topics_list}")

    def check_topic(m):
        return m.author == ctx.author and m.content.isdigit()

    chosen_topic = None
    while chosen_topic is None:
        try:
            topic_msg = await client.wait_for('message', timeout=60.0, check=check_topic)
            user_input = topic_msg.content

            if not user_input.isdigit():
                await ctx.send(f"❌ **Invalid input**: `{user_input}` is not a valid number. Please select a valid topic number from the list.")
                continue  

            chosen_topic = user_input

            if chosen_topic not in topics:
                await ctx.send(f"❌ **Invalid topic number**: `{chosen_topic}`. Please select a valid topic from the list.")
                chosen_topic = None  
            else:
                topic_questions = [q for q in multi_choice_qas if q["topic"] == chosen_topic]

                if len(topic_questions) < 10:
                    await ctx.send(f"⚠️ The selected topic **'{topics[chosen_topic]}'** does not have enough questions. It only has **{len(topic_questions)}** questions, and at least 10 are required for the skill check.")
                    await ctx.send("🚫 **This topic is not available for the skill check at the moment.** Please select another topic from the list or choose a valid number.")
                    chosen_topic = None  
                else:
                    await ctx.send(f"📝 You have chosen: **{topics[chosen_topic]}** with **{len(topic_questions)}** questions.")
        except asyncio.TimeoutError:
            await ctx.send("⏰ You took too long to choose a topic. Please try again.")
            game_active = False
            return

    await ctx.send("How many questions would you like for the quiz? Type `10` or `20`.")
    
    def check_question_count(m):
        return m.author == ctx.author and m.content in ["10", "20"]

    try:
        count_msg = await client.wait_for('message', timeout=30.0, check=check_question_count)
        question_count = int(count_msg.content)
    except asyncio.TimeoutError:
        await ctx.send("⏰ You took too long to choose the number of questions. Please try again.")
        game_active = False
        return

    if len(topic_questions) > question_count:
        topic_questions = random.sample(topic_questions, question_count)
    else:
        await ctx.send(f"There are only **{len(topic_questions)}** questions available for this topic.")

    correct_answers = 0
    total_questions = len(topic_questions)
    user_answers = []  
    correct_responses = []  

    await ctx.send(f"⏳ **You have 1 minute per question. Good luck!**")

    for idx, question in enumerate(topic_questions, 1):
        qa_text = f"❓ **Q{idx}: {question['question']}**\n" + "\n".join(question['choices'])
        question_message = await ctx.send(qa_text)

        reactions = {'🇦': 'A', '🇧': 'B', '🇨': 'C', '🇩': 'D'}
        for emoji in reactions:
            await question_message.add_reaction(emoji)

        def check_reaction(reaction, user):
            return user == ctx.author and str(reaction.emoji) in reactions

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check_reaction)
        except asyncio.TimeoutError:
            user_answers.append("Timeout")
            correct_responses.append({
                "question": question["question"],
                "correct": question["correct"],
                "explanation": question["explanation"]
            })
        else:
            user_answers.append(reactions[str(reaction.emoji)])
            correct_responses.append({
                "question": question["question"],
                "correct": question["correct"],
                "explanation": question["explanation"]
            })

            if reactions[str(reaction.emoji)] == question["correct"]:
                correct_answers += 1

    await ctx.send("📝 **Quiz Completed! Please wait for the detailed results...**")

    # Prepare result summary
    result_summary = f"🎉 **Quiz Completed!** 🎉\n\n"
    result_summary += f"🏆 **You answered {correct_answers}/{total_questions} questions correctly!** 🏆\n\n"

    # Show correct answers and explanations
    result_summary += f"📊 **Detailed Results:** 📊\n\n"
    for idx, response in enumerate(correct_responses, 1):
        result_summary += f"🔹 **Q{idx}:** {response['question']}\n"
        result_summary += f"  ❌ Your answer: {user_answers[idx-1]}\n" if user_answers[idx-1] != response['correct'] else f"  ✅ Your answer: {user_answers[idx-1]}\n"
        result_summary += f"  ✅ Correct answer: {response['correct']}\n"
        result_summary += f"  ℹ️ Explanation: {response['explanation']}\n\n"

    # Send the result summary in chunks if it exceeds the Discord message limit
    await send_long_message(ctx, result_summary)

    await ctx.send(" !!! PLEASE WAIT A FEW SECONDS FOR DETAILED ANALYSIS !!! \n")

    # Collect details for ChatGPT analysis
    wrong_answers = [r for r, a in zip(correct_responses, user_answers) if a != r['correct']]
    timeouts = user_answers.count("Timeout")

    # ChatGPT performance analysis request
    messages = [
        {
            "role": "user", 
            "content": (
                f"I answered {correct_answers}/{total_questions} questions correctly. "
                f"I had {len(wrong_answers)} wrong answers and {timeouts} timeouts. "
                "Here are the details of my wrong answers:\n" +
                "\n".join([f"Question: {r['question']}\nYour answer: {a}\nCorrect answer: {r['correct']}" for r, a in zip(wrong_answers, user_answers) if a != r['correct']])
            )
        }
    ]
    api_response = send_to_chatGpt(messages)
    await ctx.send(api_response)

    game_active = False

# Start the bot
client.run(DISCORD_TOKEN)