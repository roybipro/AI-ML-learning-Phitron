import streamlit as st
from gtts import gTTS
import io

text = "Hello, this is a test of the gTTS library. It converts text to speech."

speech = gTTS(text,lang='en',slow=False)


audio_buffer = io.BytesIO()

speech.write_to_fp(audio_buffer)

st.audio(audio_buffer)