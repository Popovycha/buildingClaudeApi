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

def chat(messages, system=None, stop_sequences=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system is not None:
        params["system"] = system
    if stop_sequences is not None:
        params["stop_sequences"] = stop_sequences

    message = client.messages.create(**params)
    # content can include non-text blocks (e.g. thinking), so keep only text
    return "".join(block.text for block in message.content if block.type == "text")

def stop_sequences(prompt):
    """Get JSON back using a stop sequence (no assistant prefill needed)."""
    messages = []
    add_user_message(messages, f"{prompt}\nPut the JSON inside <json></json> tags.")
    # Generation stops right before </json>, so nothing after the JSON comes back
    text = chat(messages, stop_sequences=["</json>"])
    return text.split("<json>", 1)[-1].strip()

if __name__ == "__main__":
    messages = []

    add_user_message(messages, "Write a 1 sentence description of a fake database")

    stream = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        stream=True,    
    )

    for event in stream:
        print(event)

    messages = []
    add_user_message(messages, "Write a 1 sentence description of a fake database")
    with client.messages.stream(
        model=model,
        max_tokens=1000,
        messages=messages,
    ) as stream:
        for text in stream.text_stream:
            # print(text, end="", flush=True)
            pass
    # stream.get_final_message()


    text = stop_sequences("Generate a very short event bridge rule as json")
    print(text)

    import json
    data = json.loads(text)
    print(data)

# Exercise 
messages = []
prompt = """
Generate three different sample AWS CLI commands. Each should be very short.
Put only the commands, one per line, inside <commands></commands> tags.
"""
add_user_message(messages, prompt)
# No prefill (unsupported by this model) - stop at the closing tag instead
text = chat(messages, stop_sequences=["</commands>"])
print(text.split("<commands>", 1)[-1].strip())