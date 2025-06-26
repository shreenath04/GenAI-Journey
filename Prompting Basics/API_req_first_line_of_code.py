import google.generativeai as genai
import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
api_key_path = script_dir / "apikey.txt"

with open(api_key_path, "r") as f:
    API_KEY = f.read().strip()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Generate a python code to print 'Hello World'")

print(response.text)

