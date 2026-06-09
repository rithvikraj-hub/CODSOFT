import datetime
import random

print("=" * 50)
print("        WELCOME TO SMART CHATBOT")
print("Type 'bye' to exit the chatbot")
print("=" * 50)

greetings = [
    "Hello! How can I help you today?",
    "Hi there! Nice to meet you.",
    "Hey! What can I do for you?"
]

while True:
    user = input("\nYou: ").lower().strip()

    # Greetings
    if user in ["hi", "hello", "hey"]:
        print("ChatBot:", random.choice(greetings))

    # How are you
    elif "how are you" in user:
        print("ChatBot: I'm doing great! Thanks for asking.")

    # Name
    elif "your name" in user:
        print("ChatBot: My name is Smart ChatBot.")

    # Age
    elif "your age" in user:
        print("ChatBot: I don't have an age like humans.")

    # Creator
    elif "who created you" in user or "developer" in user:
        print("ChatBot: I was created using Python programming.")

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("ChatBot: Current time is", current_time)

    # Date
    elif "date" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("ChatBot: Today's date is", current_date)

    # Python
    elif "python" in user:
        print("ChatBot: Python is a popular programming language.")
        print("ChatBot: It is used for AI, Machine Learning, Web Development, and Automation.")

    # AI
    elif "artificial intelligence" in user or "ai" in user:
        print("ChatBot: AI stands for Artificial Intelligence.")
        print("ChatBot: It enables machines to perform tasks that normally require human intelligence.")

    # Machine Learning
    elif "machine learning" in user:
        print("ChatBot: Machine Learning is a branch of AI.")
        print("ChatBot: It helps computers learn from data without explicit programming.")

    # College
    elif "college" in user:
        print("ChatBot: College is a place where students gain knowledge and skills.")

    # Internship
    elif "internship" in user:
        print("ChatBot: Internships help students gain practical experience and improve their skills.")

    # Courses
    elif "course" in user:
        print("ChatBot: Popular courses include Python, Data Science, AI, ML, Web Development, and Cloud Computing.")

    # Motivation
    elif "motivate me" in user:
        print("ChatBot: Success comes from consistency, not perfection.")
        print("ChatBot: Keep learning and never stop improving!")

    # Joke
    elif "joke" in user:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? It caught a virus!",
            "Why was the Java developer sad? Because he didn't get Python."
        ]
        print("ChatBot:", random.choice(jokes))

    # Favorite color
    elif "favorite color" in user:
        print("ChatBot: I like all colors because I'm a chatbot!")

    # Weather
    elif "weather" in user:
        print("ChatBot: I cannot check live weather, but you can use a weather website or app.")

    # Calculator
    elif "calculate" in user:
        try:
            expression = user.replace("calculate", "")
            result = eval(expression)
            print("ChatBot: The answer is", result)
        except:
            print("ChatBot: Please enter a valid mathematical expression.")

    # Skills
    elif "what can you do" in user:
        print("ChatBot: I can:")
        print("- Greet you")
        print("- Tell date and time")
        print("- Answer simple questions")
        print("- Tell jokes")
        print("- Motivate you")
        print("- Perform basic calculations")

    # Help
    elif "help" in user:
        print("\nChatBot Commands:")
        print("1. hello / hi")
        print("2. how are you")
        print("3. your name")
        print("4. your age")
        print("5. who created you")
        print("6. time")
        print("7. date")
        print("8. python")
        print("9. ai")
        print("10. machine learning")
        print("11. internship")
        print("12. motivate me")
        print("13. joke")
        print("14. calculate 5+10")
        print("15. what can you do")
        print("16. bye")

    # Exit
    elif user == "bye":
        print("ChatBot: Goodbye! Have a wonderful day.")
        break

    # Unknown
    else:
        print("ChatBot: Sorry, I don't understand that.")
        print("ChatBot: Type 'help' to see available commands.")
