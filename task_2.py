# Simple Chatbot

# Predefined rules and responses
rules = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi! What's on your mind?",
    "send me jok":"love is blind",
    "how are you": "I'm doing great, thanks! How about you?",
    "what's your name": "My name is CHAND, nice to meet you!",
    "quit": "Goodbye! It was nice chatting with you.",
    "nice to meet you":"It was nice chat with you",
    "about you":"Iam ! CHAND version 3.0 an AI Assistant",
    "default": "I didn't understand that. Can you please rephrase?"
}

def respond(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user input matches any of the predefined rules
    for rule in rules:
        if rule in user_input:
            return rules[rule]

    # If no match is found, return the default response
    return rules["default"]

def chatbot():
    print(" \n Welcome to CHAND! I'm here to help.")
    while True:
        user_input = input("Darsh: ")
        response = respond(user_input)
        print("CHAND:", response)
        if user_input.lower() == "quit":
            break

# Run the chatbot
chatbot()