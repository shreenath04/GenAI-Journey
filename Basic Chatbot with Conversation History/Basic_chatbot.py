'''
Here I ahve created a basic chatbot by using 
Google Gemini API, I learned how to generate API keys
use them, keep them secure and get response from the LLM
'''

# importing necessary libraries
import google.generativeai as genai
import os
from pathlib import Path

# providing API key
script_dir = Path(__file__).resolve().parent
api_key_path = script_dir / "apikey.txt"

with open(api_key_path, "r") as f:
    API_KEY = f.read().strip()

genai.configure(api_key=API_KEY)

# selecting model to run
model = genai.GenerativeModel('gemini-1.5-flash')

# Input and response loop
print("Basic chatbot using Goggle Gemini API\nTo quit the chat please type 'exit' or 'bye'")

while True:
    user_inp = input("You: ")
    if user_inp.lower() in ["exit", "bye"]:
        print("Chatbot: See you back soon\nBye !")
        break
    try:
        response = model.generate_content(user_inp)
        reply = response.text.strip()
        print("Chatbot: ", reply)
    except Exception as e:
        print("Chatbot: Oops! Something went wrong.", str(e))