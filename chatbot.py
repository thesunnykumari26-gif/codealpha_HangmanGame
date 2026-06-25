# =============================
# CodeAlpha Task 4 - Basic Chatbot
# =============================

def chatbot():
    print("🤖 ChatBot: Hello! I am your basic chatbot.")
    print("Type 'bye' to exit the chat.\n")

    while True:
        user_input = input("You: ").lower()

        # Greetings
        if user_input in ["hello", "hi", "hey"]:
            print("🤖 ChatBot: Hello there!")

        # Asking about chatbot
        elif user_input == "how are you":
            print("🤖 ChatBot: I am fine. Thanks for asking!")

        # Asking name
        elif user_input == "what is your name":
            print("🤖 ChatBot: My name is CodeAlpha Bot.")

        # Asking about creator
        elif user_input == "who created you":
            print("🤖 ChatBot: I was created using Python programming.")

        # Asking time
        elif user_input == "what can you do":
            print("🤖 ChatBot: I can chat with you using predefined responses.")

        # Help command
        elif user_input == "help":
            print("🤖 ChatBot: You can ask things like:")
            print("- hello")
            print("- how are you")
            print("- what is your name")
            print("- who created you")
            print("- what can you do")
            print("- bye")

        # Exit condition
        elif user_input == "bye":
            print("🤖 ChatBot: Goodbye! Have a nice day 😊")
            break

        # Unknown input
        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")

# Run chatbot
chatbot()