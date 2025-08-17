# Rule-based Chatbot

# Dictionary of rules (user_input : response)
responses = {
    "hi": "Hello! 👋",
    "hello": "Hi there! 😊",
    "hey": "Hey! How are you?",
    "how are you": "I'm just a bot, but I'm doing fine. Thanks for asking! 🤖",
    "what is your name": "I'm your friendly chatbot 🤖",
    "bye": "Goodbye! 👋 Take care.",
    "thank you": "You're welcome! 🙌"
}

print("🤖 Rule-based Chatbot (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "quit":
        print("Bot: Bye! 👋")
        break

    # If exact match found in dictionary
    if user_input in responses:
        print("Bot:", responses[user_input])
    else:
        print("Bot: Sorry, I don’t understand that yet 😅")



