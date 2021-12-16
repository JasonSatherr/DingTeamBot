# from camera import Camera
# from face_detector import FaceFinder
from discord_bot import DiscordBot
def main():
    """The main file will run everything
    """
    # cam = Camera()
    # stream = cam.getPictureStream()
    # faceFinder = FaceFinder()
    # numFaces = faceFinder.getNumFacesFromImage(stream)
    # print('we found '+ str(numFaces)+ ' faces')

    #Start the discord bot...
    discordBot = DiscordBot()
    #discordBot.giveDripPic(stream)
    discordBot.start()
    



if __name__ == "__main__":
    main()