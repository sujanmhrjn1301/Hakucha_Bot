from dotenv import load_dotenv
import openai
import requests
import os


load_dotenv()

openai.api_key= os.getenv("CHATGPT_API_KEY")


def chatgpt_response(prompt): #taking response or prompt from the user
         
        response= openai.Completion.create(
            model= "text-davinci-003",
            prompt= prompt,      #prompt variable takes prompt i.e user message
            temperature=1,
            max_tokens= 100
        )
        response_dict= response.get("choices")
        if response_dict and len(response_dict) > 0: #only if there is response it will respond
            prompt_response = response_dict[0]["text"]   # ai response equal to responce dict
        return prompt_response

