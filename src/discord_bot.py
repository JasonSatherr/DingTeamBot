import discord
from discord.ext import commands, tasks
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
        
        #temp code below...
        self.CHANNEL = config('CHANNEL_ID')
        # self.my_annoying_task.start()


    # @tasks.loop(seconds=6) # task runs every 60 seconds
    # async def my_annoying_task(self):
    #     channel = self.bot.get_channel(920905958090240021) # channel ID goes here
    #     await channel.send("are you annoyed yet?")
    #     print("sent")

    # @my_annoying_task.before_loop
    # async def before_my_task(self):
    #     await self.bot.wait_until_ready() # wait until the bot logs in
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
        async def dripPic(ctx, filename = 'drip', mode):  #Be sure to disable this command or make it admin exclusive...
            """Close the bot 3 seconds after it's ready, just for the sake of the example."""
            await ctx.send("Making a drip pic")
            self.smartCamera.takeNewPicture()
            pic = self.smartCamera.getBasePicture()
            dripPic = discord.File(fp=pic, filename=str(filename)+'.jpeg', spoiler=False)
            await ctx.send(file = dripPic)

        @self.bot.command()
        async def orwell(ctx, filename = 'drip'):  #Be sure to disable this command or make it admin exclusive...
            """Close the bot 3 seconds after it's ready, just for the sake of the example."""
            await ctx.send("Making a orwell pic")
            self.smartCamera.takeNewPicture()
            pic = self.smartCamera.getProcessedPhotoBare()
            dripPic = discord.File(fp=pic, filename=str(filename)+'.jpeg', spoiler=False)
            await ctx.send(file = dripPic)
            await ctx.send(f'We found {self.smartCamera.getNumBareFaces()} faces.')




    
