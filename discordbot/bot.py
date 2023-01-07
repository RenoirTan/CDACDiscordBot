"""
`discordbot.bot`

This module contains functions and other definitions for the discord bot.
"""


import discord
from discord.ext import commands


# Permissions to access Discord's API
intents = discord.Intents.default()
intents.message_content = True # We want to see what a user has written


# Command prefix (e.g. "!" for !ping)
bot = commands.Bot(command_prefix="!", intents=intents)


# What to do when bot has come online
@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}")


def run_bot(token):
    """
    Run the bot with a provided token.
    """
    bot.run(token)