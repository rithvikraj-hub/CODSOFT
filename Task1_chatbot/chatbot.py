print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("ChatBot: Hello! How can I help you?")
    
    elif "how are you" in user:
        print("ChatBot: I'm fine, thank you! How are you?")
    
    elif "your name" in user:
        print("ChatBot: My name is ChatBot.")
    
    elif "help" in user:
        print("ChatBot: I can answer simple questions like greetings, my name, and how I am.")
    
    elif "bye" in user:
        print("ChatBot: Goodbye! Have a nice day.")
        break
    
    else:
        print("ChatBot: Sorry, I don't understand that.")
