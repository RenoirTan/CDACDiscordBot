"""
`discordbot.bot`

This module contains functions and other definitions for the discord bot.
"""

from random import randint

import discord
from discord.ext import commands

from discordbot.util import railfence_encode, bubble_sort, best_fit_emoji, emoji_list


# Permissions to access Discord's API
intents = discord.Intents.default()
intents.message_content = True # We want to see what a user has written
intents.members = True # see members' actions
intents.guilds = True # access to guild's stuff
intents.emojis_and_stickers = True


# Command prefix (e.g. "!" for !ping)
bot = commands.Bot(command_prefix="!", intents=intents)


async def send_error(ctx: commands.Context, message: str):
    """
    Create an embedded message for an error and then send it.
    """
    embed = discord.Embed(color=0xFF0000, title=message)
    await ctx.send(embed=embed)


# What to do when bot has come online
@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}")
    game = discord.Game("with the API")
    await bot.change_presence(activity=game)


# When a member joins
@bot.event
async def on_member_join(member: discord.Member):
    # Get default channel
    system_channel = member.guild.system_channel
    # Check if we are allowed to send messages
    if system_channel.permissions_for(member.guild.me).send_messages:
        await system_channel.send(f"<@{member.id}> has joined {member.guild.name}.")


# Feature 1
# Ping the bot
@bot.command()
async def ping(ctx):
	await ctx.send('Pong')


# Feature 2
# Calculate the result of an operation on 2 numbers.
# Example: !calc 1 + 2
@bot.command()
async def calc(ctx: commands.Context, arg1: str, operator: str, arg2: str):
    try:
        num1 = float(arg1)
    except:
        await send_error(ctx, "Your first number is not a number.")
        return
    try:
        num2 = float(arg2)
    except:
        await send_error(ctx, "Your second number is not a number.")
        return
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        await send_error(ctx, "We don't allow that kind of operation yet.")
        return

    await ctx.send(f"{arg1} {operator} {arg2} = {result}")


# Feature 3
# Guess the number (integer)
@bot.command()
async def guess(ctx: commands.Context, guess: str):
    # number = 7
    number = randint(0, 9) # 0 to 9 inclusive
    try:
        guess = int(guess)
    except:
        await send_error(ctx, "guess is not an integer")
        return
    if guess < number:
        await ctx.send("too low")
    elif guess > number:
        await ctx.send("too high")
    else: # guess == number
        await ctx.send("yay")


# Feature 4
# Reply to member with what they said
@bot.command()
async def parrot(ctx: commands.Context, *args: str):
    message = ctx.message.content[8:] # get rid of "!parrot "
    # we get an error if we try to send a blank message, so we have to handle
    # that case separately
    if len(message) == 0:
        await send_error(ctx, "You sent an empty message!")
    else:
        await ctx.send(message)


# Feature 5
@bot.command()
async def fizzbuzz(ctx: commands.Context, limit: str):
    try:
        limit = int(limit)
    except:
        await send_error(ctx, "Limits must be a positive integer")
        return
    if limit <= 0:
        await send_error(ctx, "Limits must be a positive integer")
        return
    
    message = ""
    for i in range(limit):
        message += str(i)
        if i % 3 == 0:
            message += "Fizz"
        if i % 5 == 0:
            message += "Buzz"
        message += "\n"
    await ctx.send(message)


# Feature 6
# Sort a list of numbers using bubble sort
@bot.command()
async def bubble(ctx: commands.Context, *numbers: str):
    sequence = []
    for number in numbers:
        try:
            number = float(number)
        except:
            await send_error(ctx, f"{number} is not a number")
            return
        sequence.append(number)
    if len(sequence) == 0:
        await send_error(ctx, "Nothing to sort")
        return

    sequence = bubble_sort(sequence)
    s_sequence = list(map(str, sequence))
    await ctx.send("Sorted: " + " ".join(s_sequence))


# Feature 7
# Convert plaintext to crypttext using railfence encoding
@bot.command()
async def railfence(ctx: commands.Context, n_rails: str, *words: str):
    try:
        n_rails = int(n_rails)
    except:
        await send_error(ctx, "Rails must be a positive integer")
        return
    if n_rails <= 0:
        await send_error(ctx, "Rails must be a positive integer")
        return
    
    plaintext = "".join(words)
    
    if len(plaintext) == 0:
        await send_error(ctx, "Your message cannot be empty")
        return
    
    # See util.py
    crypttext = railfence_encode(n_rails, plaintext)
    
    await ctx.send(crypttext)


# Feature 8
@bot.command()
async def emojify(ctx: commands.Context, *args: str):
    message = ctx.message.content[9:] # get rid of "!emojify "
    # we get an error if we try to send a blank message, so we have to handle
    # that case separately
    if len(message) == 0:
        await send_error(ctx, "You sent an empty message!")
    else:
        words = message.split(' ') #gives an array of each word that we can iterate through
        emojifiedreply = ''
        options = emoji_list()
        for word in words:
            emojifiedreply += word #reconstructs the original message
            bfe = best_fit_emoji(word, options)
            emojifiedreply += " " + bfe + " " #with the emoji behind it
        await ctx.send(emojifiedreply)


# Run the bot
from discordbot.secrets import token

bot.run(token)
