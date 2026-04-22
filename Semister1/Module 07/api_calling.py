from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")


#initializing the client
client = genai.Client(api_key = my_api_key)



#note generation
def generate_note_summary(images):
    
    prompt ="""Summarize the pictures in note formet at max 100 words,
    make sure to markdown to deffrentiate diffrent sections"""
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images,prompt]
    )
    
    return response.text