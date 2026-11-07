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

# NOTE: why there is no `temperature` parameter here
# The Claude API removed the sampling parameters `temperature`, `top_p` and `top_k`
# (API version 2026-10-21). Sending any of them now returns a 400 error on every
# model, even at the default value. The anthropic SDK (2.x) also dropped the
# argument, so passing temperature=... raises:
#   TypeError: Messages.create() got an unexpected keyword argument 'temperature'
# Claude Sonnet 5.5 only accepted the default value anyway.
#
# To get a similar effect, steer the model with the prompt instead:
#   - more predictable: system="Give the single most conventional answer. Be concise."
#   - more creative:    ask for "an unusual, surprising idea" or "5 very different ideas"
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


    add_user_message(messages, "Generate a one sentence movie idea")

    answer = chat(messages)

    print(answer)