from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant for university students."},
        {"role": "user", "content": "Why should I join IE University's AI Hackathon?"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
