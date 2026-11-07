from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  # reads ANTHROPIC_API_KEY from .env

client = Anthropic()
model = "claude-sonnet-5-5"

def add_user_message(message, text):
    user_message = {"role": "user", "content": text}
    message.append(user_message)

def add_assistant_message(message, text):
    assistant_message = {"role": "assistant", "content": text}
    message.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    # content can include non-text blocks (e.g. thinking), so keep only text
    return "".join(block.text for block in message.content if block.type == "text")

if __name__ == "__main__":
    #Make a starting list of messages
    messages = []

    #add in the initial user question of "Define quantum computing in one sentence"
    add_user_message(messages, "Define quantum computing in one sentence")

    #pass the list of messages to the chat function and get the response
    answer = chat(messages)

    # Take answer and add it as assistant message to the list of messages
    add_assistant_message(messages, answer)

    #add in the user's follow up question
    add_user_message(messages, "Write another sentence")

    #Call chat again with the updated list of messages and get the final answer
    answer = chat(messages)

    print(answer)
