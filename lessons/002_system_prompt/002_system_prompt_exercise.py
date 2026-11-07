from system_prompt import add_user_message, chat

messages = []

add_user_message(messages, "Write a Python function that checks a string for duplicate characters.")

answer = chat(messages, system="You are a python engineer who writes very concise code.")

print(answer)