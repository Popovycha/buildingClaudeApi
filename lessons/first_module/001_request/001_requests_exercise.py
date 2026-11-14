from request import add_user_message, add_assistant_message, chat

#Make an intiial list of messages
messages = []

# Use a 'while True' loop to run the chatbot forever
while True:
    #Get User input
    user_input = input(">")
    print(">", user_input)

    # Add user input to the list of messages
    add_user_message(messages, user_input)

    # Call Claude with the 'chat' function
    answer = chat(messages)

    #Add generated text to the list of messages
    add_assistant_message(messages, answer)

    #Print the generated text
    print("---")
    print(answer)
    print("---")