from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

completion = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Napisz kod w pythonie ktory dodaje dwie liczby"},
  ]
)

print(completion.choices[0].message.content)
print(f'tokens used: {completion.usage.total_tokens}')
