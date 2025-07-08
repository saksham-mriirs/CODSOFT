def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you today?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm Chatbot 101, your virtual assistant.")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")

        elif "help" in user_input:
            print("Chatbot: Sure! I can answer questions like 'what's your name?', 'how are you?', or 'what can you do?'")

        elif "what can you do" in user_input:
            print("Chatbot: I can chat with you and respond to simple questions.")

        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        else:
            print("Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
