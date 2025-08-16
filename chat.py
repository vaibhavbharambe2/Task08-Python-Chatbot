

def chatbot():
    print("Hello! I'm a simple rule-based chatbot. Type 'exit' to quit.")
    
    while True:
        user_input = input("User: ").lower()

        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected!")
        elif 'your name' in user_input:
            print("Chatbot: I'm a simple rule-based chatbot created using Python.")
        elif 'weather' in user_input:
            print("Chatbot: I don't have real-time weather data, but it's always sunny in the world of code!")
        elif 'thank' in user_input:
            print("Chatbot: You're welcome! Happy to help.")
        elif 'what is your purpose' in user_input:
            print("Chatbot: I'm here to demonstrate a simple rule-based chatbot built with Python.")
        elif 'help' in user_input:
            print("Chatbot: You can ask me things like 'hello', 'how are you', or 'what is your name'.")
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")


chatbot()
