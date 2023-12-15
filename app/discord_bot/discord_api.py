from dotenv import load_dotenv
import discord
import openai
import requests
import os
from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client): # MyClient is a sub class of discord.client
    async def on_ready(self):
        print("Successfully logged in as:", self.user)
        

#for messages
    async def on_message(self, message):
        print(message.content)
        if message.author== self.user:      #self.user is the bot here
            return
        command, user_message = None, None
        
    
        for text in ['/ai','/bot','/chatgpt']:
            if message.content.startswith(text):
                #splitting command and user message
                command= message.content.split(' ')[0]  # [0] means it will read the first \ai as command and other remaining as user message
                user_message= message.content.replace(text,'')
                print(command,user_message)
                
                
        if command== '/ai' or command== '/bot' or command== '/chatgpt':
            bot_response = chatgpt_response(prompt= user_message) #prompt value is the user's message
            await message.channel.send(f"{bot_response}")
            
intents = discord.Intents.all()
intents.message_content= True

client= MyClient(intents=intents)   #instance of the class MyClient
            
            