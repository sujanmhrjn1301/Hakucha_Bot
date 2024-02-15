import discord
from openai import OpenAI
import os
from dotenv import load_dotenv
from discord.ext import tasks
from app.openai_api.openai_api import Bll

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
   # Run code when bot is ready
   async def on_ready(self):
       await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= "with you"))
       print(f"{bot.user} is now ready to respond! ")

   # Run code when bot joins a guild
   async def on_guild_join(self,guild):
       channel= guild.system_channel
       if channel:
           await channel.send(f"https://tenor.com/view/entrance-confident-im-here-woody-toy-story-gif-11881136")

   # Run code when a message is sent
   async def on_message(self,message):
       # Ignore bot's own messages
       if message.author== bot.user:
           return

       # Convert message content to lowercase
       content= message.content.lower()

       # Define keywords and image command keywords
       words=["/helpme","/ask","/describe"]
       img_cmds=["/make","/create","/generate"] 

       # Check if bot is mentioned or keywords are present
       try:
           if (bot.user.mentioned_in(message) and content) or any(word in content for word in words):
               print(f"{message.author.name} searched for: {content}")
               await message.channel.send("Thinking...")
               # Get AI response using Bll class
               AI_Response =  Bll.openAI_response(content)
               await message.channel.send(AI_Response)
       except Exception as e:
           print(f"Error: {e}")