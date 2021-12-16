import discord
from discord.ext import commands
from decouple import config
import asyncio
description = '''Coolest Boba Bot ever.

(Tu won't let me call her an e-girl)'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def checkStore(ctx):
    """Tells how many people are in the store"""
    await ctx.send("Can't see the store right now :(")



@bot.command()
async def farewell(ctx):  #Be sure to disable this command or make it admin exclusive...
    """Close the bot 3 seconds after it's ready, just for the sake of the example."""
    await ctx.send("Bye")
    await asyncio.sleep(3)
    await bot.close()

DISCORD_TOKEN = config('DISCORD_TOKEN')

bot.run(DISCORD_TOKEN)

