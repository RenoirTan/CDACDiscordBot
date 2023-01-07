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


# What to do when bot has come online
@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}")


# When a member joins
@bot.event
async def on_member_join(member: discord.Member):
    # Get default channel
    system_channel = member.guild.system_channel
    # Check if we are allowed to send messages
    if system_channel.permissions_for(member.guild.me).send_messages:
        await system_channel.send(f"<@{member.id}> has joined {member.guild.name}.")


def run_bot(token):
    """
    Run the bot with a provided token.
    """
    bot.run(token)