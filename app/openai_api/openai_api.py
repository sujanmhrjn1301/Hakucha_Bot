from dotenv import load_dotenv
from openai  import OpenAI
import os
import openai

load_dotenv() # load environment variables

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY')) # create OpenAI client

class Bll: # define Bll class
    def __init__(self, client): # constructor
        self.client = client # initialize client

    @staticmethod # static method
    def openAI_response(content): # method to get OpenAI response
        try: # try block
            completion = client.chat.completions.create( # create completion
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "user", "content": content}],
                max_tokens=100,
                stop=None,
                n=1,
                temperature=0.8,
            )
            reply = completion.choices[0].message.content # get reply
            return reply # return reply
        except openai.OpenAIError as e: # exception handling
            print(f"An OpenAI error occurred: {str(e)}")
            return str(e)
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return str(e)

    @staticmethod # static method
    def openAI_image(content): # method to generate image
        completion = client.images.generate( # generate image
            model="dall-e-3",
            prompt=content,
            n=1,
            size="1024x1024",
        )
        try:
            reply = completion.data[0].url # get image URL
            return reply
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return str(e) 