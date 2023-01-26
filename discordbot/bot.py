"""
`discordbot.bot`

This module contains functions and other definitions for the discord bot.
"""


import discord
from discord.ext import commands


# Permissions to access Discord's API
intents = discord.Intents.default()
intents.message_content = True # We want to see what a user has written
intents.members = True # see members' actions
intents.guilds = True # access to guild's stuff


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


# Calculate the result of an operation on 2 numbers.
# Example: !calc 1 + 2
@bot.command()
async def calc(ctx: commands.Context, arg1: str, operator: str, arg2: str):
    try:
        num1 = float(arg1)
    except:
        await send_error(ctx, "Your first number is not a number.")
    try:
        num2 = float(arg2)
    except:
        await send_error(ctx, "Your second number is not a number.")
    
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


# Grab all letters in the text that comes after !letters and
# sum the value of the letters.
# The value of each letter is their position in the alphabet (e.g. A = 1, B = 2)
@bot.command()
async def letters(ctx: commands.Context, *args: str):
    total = 0
    
    # Get each word in the message
    for word in args:
        
        # Get each character in each word
        for character in word:
            
            # if character is not a letter, then skip
            if not character.isalpha():
                continue
            
            # convert letter to uppercase
            letter = character.upper()
            
            # ord() gets the position of the letter in the ASCII alphabet
            # the position of uppercase 'A' is 65, so to get the position of
            # the letter in the normal alphabet, we minus 64 to get 1
            value = ord(letter) - 64
            
            # add to sum
            total += value
    await ctx.send(f"Total value: {total}")


def run_bot(token):
    """
    Run the bot with a provided token.
    """
    bot.run(token)