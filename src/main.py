import sys
sys.path.append('./src/imageProcessing')  #FIX THIS FILE HIERARCHY DEPENDANT IMPORT!!!
from cameraTester import cameraTester

from discord_bot import DiscordBot
def main():
    """The main file will run everything
    """
    # camTest = cameraTester()
    # camTest.runAWBTests()

    discordBot = DiscordBot()
    discordBot.start()
    



if __name__ == "__main__":
    main()