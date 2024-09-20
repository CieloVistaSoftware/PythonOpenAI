import openai
import os

# Ensure the OpenAI API key is set in the environment variables
if not os.getenv("OpenAIKey2"):
    raise EnvironmentError("Please set the OpenAIKey2 environment variable.")

# Set up your API key from an environment variable
openai.api_key = os.getenv("OpenAIKey2")

from openai import OpenAI

print(f"OpenAI API Key: {openai.api_key}")
question = "What is the capital of the United States?"
client = OpenAI()
response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question },
            {
                "role": "assistant",
                "content": ""
            },
            {"role": "user", "content": "When was it founded?"},
            {"role": "user", "content": "Who were famous people born there?"},
        ],
    )
length = len(response.choices)
print(f'Choices length: {length}')
answer = response.choices[0].message.content
print(f"response: {answer}")
 
