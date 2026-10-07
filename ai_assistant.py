from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

model = os.getenv("MODEL")
question = input("Hello! How can I help you?")
while question != "exit":
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
             
                "role": "user",
                "content": question
            }
        ]
    )
    print(response.choices[0].message.content)
    question = input("How can I help you next?")

