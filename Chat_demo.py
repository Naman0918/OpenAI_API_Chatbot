import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# ChatCompletion is used to generate a response to a prompt not Completion.
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Give me 3 idea to learn ML "}]
    )

print(completion.choices[0].message.content)