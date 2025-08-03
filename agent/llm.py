from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def query_llm(prompt: str, model="llama3-8b-8192") -> str:
    messages = [
        {"role": "system", "content": "You are a reasoning assistant."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.4,
    )

    return response.choices[0].message.content.strip()
