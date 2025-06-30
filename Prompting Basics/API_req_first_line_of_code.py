'''
Here I am generating my first line of code using an LLM,
I learned from the documentation and I still need to understand this.
But hey! At least I followed the steps and it worked!
'''
#importing necessary libraries
import google.generativeai as genai
import os
from pathlib import Path

# securly accessing api key
script_dir = Path(__file__).resolve().parent
api_key_path = script_dir / "apikey.txt"

with open(api_key_path, "r") as f:
    API_KEY = f.read().strip()

# following the documentation
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Generate a python code to print 'Hello World'")

print(response.text)

