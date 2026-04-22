import streamlit as st
from PIL import Image
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

# Initialize client
client = genai.Client(api_key=my_api_key)

# Upload images
uploaded_files = st.file_uploader(
    "Choose images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

print(type(uploaded_files))  # Check the type of uploaded_files

if uploaded_files:
    # Convert uploaded files to PIL images
    pil_images = [Image.open(file) for file in uploaded_files]

    prompt = """Summarize the pictures in note format (max 100 words).
Use markdown to differentiate sections."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=pil_images + [prompt]   # combine properly
    )

    st.text(response.text)