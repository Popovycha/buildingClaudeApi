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

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system is not None:
        params["system"] = system

    message = client.messages.create(**params)
    # content can include non-text blocks (e.g. thinking), so keep only text
    return "".join(block.text for block in message.content if block.type == "text")

if __name__ == "__main__":
    messages = []

    system = """
        You are a patient math tutor.
        Do not directly answer a student's question.
        Guide them to a solution step by step.
    """
    add_user_message(messages, "How do I solve 5x+3=2 for x?")

    answer = chat(messages, system=system)

    print(answer)
