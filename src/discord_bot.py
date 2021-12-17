import discord
from discord.ext import commands
from decouple import config
import asyncio
import sys
sys.path.append('./src/imageProcessing')
from smartCamera import smartCamera


class DiscordBot:
    def __init__(self) -> None:
            
        description = '''Coolest Boba Bot ever.

        (Tu won't let me call her an e-girl)'''
        intents = discord.Intents.default()
        self.smartCamera = smartCamera()
        self.bot = commands.Bot(command_prefix='?', description=description, intents=intents)
        self.setupEvents()
        self.setupCommands()

    def giveDripPic(self, stream):
        self.stream = stream

    def start(self):
        DISCORD_TOKEN = config('DISCORD_TOKEN')
        self.bot.run(DISCORD_TOKEN)

    def setupEvents(self):
        @self.bot.event
        async def on_ready():
            print('Logged in as')
            print(self.bot.user.name)
            print(self.bot.user.id)
            print('------')


    def setupCommands(self):

        @self.bot.command()
        async def add(ctx, left: int, right: int):
            """Adds two numbers together."""
            await ctx.send(left + right)

        @self.bot.command()
        async def checkStore(ctx):
            """Tells how many people are in the store"""
            await ctx.send("Can't see the store right now :(")



        @self.bot.command()
        async def bye(ctx):  #Be sure to disable this command or make it admin exclusive...
            """Close the bot 3 seconds after it's ready, just for the sake of the example."""
            await ctx.send("Farewell")
            await asyncio.sleep(3)
            await self.bot.close()

        @self.bot.command()
        async def dripPic(ctx, filename = 'drip'):  #Be sure to disable this command or make it admin exclusive...
            """Close the bot 3 seconds after it's ready, just for the sake of the example."""
            await ctx.send("Making a drip pic")
            cam = Camera()
            stream = cam.getPictureStream()
            stream.seek(0)
            dripPic = discord.File(fp=stream, filename=str(filename)+'.jpeg', spoiler=False)
            await ctx.send(file = dripPic)

        @self.bot.command()
        async def orwell(ctx, filename = 'drip'):  #Be sure to disable this command or make it admin exclusive...
            """Close the bot 3 seconds after it's ready, just for the sake of the example."""
            await ctx.send("Making a orwell pic")
            cam = Camera()
            stream = cam.getPictureStream()
            faceFinder = FaceFinder()
            numFaces = faceFinder.getNumFacesFromImage(stream)
            print('we found '+ str(numFaces)+ ' faces')
            stream.seek(0)
            dripPic = discord.File(fp=stream, filename=str(filename)+'.jpeg', spoiler=False)
            await ctx.send(file = dripPic)

            

    





