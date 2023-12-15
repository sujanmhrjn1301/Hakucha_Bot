from app.discord_bot.discord_api import client, discord_token

if __name__=="__main__":    #checks if the code is being run as the main program or not
    #or is it being imported as a module
    client.run(discord_token)