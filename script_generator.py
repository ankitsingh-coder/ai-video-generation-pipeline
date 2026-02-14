import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

def generate_script(topic):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": f"Write a short 1 minute YouTube video script on: {topic}"}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    print("DEBUG:", result)

    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return "Error generating script."



