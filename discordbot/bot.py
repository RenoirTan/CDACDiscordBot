"""
`discordbot.bot`

This module contains functions and other definitions for the discord bot.
"""

# Import discord here!


# Permissions to access Discord's API
intents = discord.Intents.default()
intents.message_content = True # We want to see what a user has written
intents.members = True # see members' actions
intents.guilds = True # access to guild's stuff
intents.emojis_and_stickers = True


# Command prefix (e.g. "!" for !ping)
bot = commands.Bot(command_prefix="!", intents=intents)


async def send_error(ctx, message):
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
async def on_member_join(member):
    pass


# Feature 1
# Ping the bot
@bot.command()
async def ping(ctx):
	pass


# Feature 2
# Calculate the result of an operation on 2 numbers.
# Example: !calc 1 + 2
@bot.command()
async def calc(ctx, arg1, operator, arg2):
    pass


# Feature 3
# Guess the number (integer)
@bot.command()
async def guess(ctx, guess):
    pass


# Feature 4
# Reply to member with what they said
@bot.command()
async def parrot(ctx, *args):
    pass


# Feature 5
@bot.command()
async def fizzbuzz(ctx, limit):
    pass


# Feature 6
# Sort a list of numbers using bubble sort
@bot.command()
async def bubble(ctx, *numbers):
    pass


# Feature 7
# Convert plaintext to crypttext using railfence encoding
@bot.command()
async def railfence(ctx, n_rails, *words):
    pass


# Feature 8
@bot.command()
async def emojify(ctx, *args):
    pass


# Run the bot
from discordbot.secrets import token

bot.run(token)
