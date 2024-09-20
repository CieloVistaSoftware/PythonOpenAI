# Using the OpenAPI Chat Model gpt-40-mini
## Assumption
You know enough about Python regarding using the virtual environment and the requirements.txt file.  This command will restore dependencies to the active env.

```pip install -r requirements.txt```

You know a bit about the [GPT models](https://platform.openai.com/docs/guides/text-generation/which-model-should-i-use).

## Getting Started
1. You will need to buy a subscription to OpenAi, this allows you to use their services to answer questions.
2. [Pricing](https://openai.com/chatgpt/pricing/) it is recommended you pay the $20/month fee.
3. Once you are ready, [Read the Chat Completions guide](https://platform.openai.com/docs/guides/chat-completions/overview)
4. Create a key, which will be passed to OpenAi as shown here at top of the program.

Warning: You only get one chance to save the key to a secure location. Copy it to the clipboard and immediately store it in the user environment. As seen below we stored it there with the key name being OpenAIKey2.

```python
# Ensure the OpenAI API key is set in the environment variables
if not os.getenv("OpenAIKey2"):
    raise EnvironmentError("Please set the OpenAIKey2 environment variable.")

# Set up your API key from an environment variable
openai.api_key = os.getenv("OpenAIKey2")
```
The openai.api_key is a static variable and can be set anytime.

A Sample is shown on that page:

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
```

## Messages

As shown above the messages array stores key value pairs. Any single request for
an answer can lead direct the answer based on multiple questions and giving a hint
to the "assistant". The "assistant" is where the answers are returned. You can leave this field blank or try to provide an answer, if the answer is wrong the response will indicate that. In a question and answer chatbot, this field could 
be used to attempt to submit the answer to the questions.

The question pattern is ```"role":"user", "content": "the question to ask"```

A query can have one or more questions.

## Run the program

Change the directory to the PythonLocal folder and run this command.

```... PythonLocal> python .\my.py```
