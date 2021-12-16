import discord
from discord.ext import commands
import random

description = '''Coolest Boba Bot ever.

(Tu won't let me call her an e-girl)'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


# @bot.event
# async def on_ready():
#     print('Logged in as')
#     print(bot.user.name)
#     print(bot.user.id)
#     print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run('token')

