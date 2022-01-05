# DING TEA BOT
## OBJECTIVE:
Create a bot that will use the small foot print and portability of the raspberry pi in order to
figure out how many people are in line at ding tea.  Then post the information to the discord channel
so that we can hang out in the bathroom and be aware of the store's business.

## Setup
---
1. You need a raspberry pi with a camera module.
  - You can typically but these off [Amazon](https://www.amazon.com) 
  - or [Adafruit] (https://www.adafruit.com/category/105)
2.  Next, you will need to create a discord bot.
  - Go to (this page)[https://discordpy.readthedocs.io/en/stable/discord.html] to figure out how to create a discord bot.
  - Record the token given to us.  This will be important later when we put it into a .env file.
  - Add your new favorite discord bot to your discord server.
4. Once the pi has arrived, you need to configure the raspberry pi to be able to connect to wifi or the ethernet as we will be doing most of our work through SSH.
  - If you're planning to run a completely headless build, follow this [article](https://www.seeedstudio.com/blog/2021/01/25/three-methods-to-configure-raspberry-pi-wifi/)
5. If working in a headless environment, set up VS code on the rpi and your own system so that you can SSH into the the rpi from your main work environment. [As shown here](https://code.visualstudio.com/docs/remote/ssh)
6. Make sure you can [take pictures](https://roboticsbackend.com/raspberry-pi-camera-take-picture/)
7. Next, we want to fork the repo.
8. Then, create a .env file at the root of the repo.  Inside write
    DISCORD_TOKEN=YOUR_DISCORD_TOKEN_FROM_STEP_2
8. Finally, we can run main.py
9. Congrats, your bot is now online and ready to snap pics 📸

---
# Fun time! 🥳
Use the command
  ?dripPic
in discord To have the camera take a picture of you!

Use the command
  ?orwell
in discord To have the camera take a picture and analyze for faces!

