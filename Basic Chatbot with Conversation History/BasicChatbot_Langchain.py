'''
In this file, I have researched and learned how to integrate langchian and its
gemini wrapper to add conversation history to my basic chatbot.
I learned to deep dive into docs and examples to learn 
how to implement the concept. Tempreture is used to control
the creativity or randomness in respsonse of model.
'''

#importing necessasry libraries
import os
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

#providing the API key
script_dir = Path(__file__).resolve().parent
api_key_path = script_dir / "apikey.txt"

with open(api_key_path, "r") as f:
    os.environ["GOOGLE_API_KEY"] = f.read().strip()

# Setting Gemini as the model to use
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# Memory to track conversations
memory = ConversationBufferMemory(return_messages=True)

# Creating chatbot with memory
chat = ConversationChain(llm=llm, memory=memory, verbose=False)

# Input and response loop
print("LangChain Chatbot using Gemini (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "bye"]:
        print("Chatbot: Goodbye! 👋")
        break
    try:
        response = chat.run(user_input)
        print("Chatbot:", response)
    except Exception as e:
        print("Chatbot: Something went wrong:", str(e))