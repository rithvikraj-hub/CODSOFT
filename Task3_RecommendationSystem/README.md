# Rule-Based Chatbot

## Overview

This project implements a simple Rule-Based Chatbot using Python. The chatbot interacts with users by recognizing predefined keywords and responding with appropriate messages. It uses conditional statements (`if-elif-else`) to identify user queries and generate responses.

The project demonstrates the fundamentals of Natural Language Processing (NLP), conversational AI, and user interaction through a command-line interface.

## Features

* Responds to greetings such as "Hello" and "Hi"
* Answers questions about its name
* Provides information about Artificial Intelligence (AI)
* Responds to course-related queries
* Offers help instructions to users
* Ends the conversation when the user types "bye"
* Handles unknown inputs gracefully

## Technologies Used

* Python 3
* Conditional Statements
* Basic Natural Language Processing Concepts

## Project Structure

```text
FUTURE_ML_01/
│
├── chatbot.py
├── README.md
└── requirements.txt
```

## How It Works

1. The chatbot accepts user input.
2. The input is converted to lowercase for easier matching.
3. Predefined rules are checked using conditional statements.
4. A suitable response is displayed.
5. The conversation continues until the user enters "bye".

## Sample Interaction

```text
ChatBot: Hello! Type 'bye' to exit.

You: Hi
ChatBot: Hello! How can I help you?

You: What is AI?
ChatBot: Artificial Intelligence (AI) is the simulation of human intelligence in machines that can learn, reason, and make decisions.

You: What course are you studying?
ChatBot: I am studying Artificial Intelligence and Machine Learning (AI & ML).

You: Bye
ChatBot: Goodbye! Have a nice day.
```

## Learning Outcomes

* Understanding chatbot design
* Implementing rule-based conversation flow
* Using conditional logic in Python
* Introduction to Natural Language Processing concepts
* Building interactive command-line applications

## Future Enhancements

* Add more conversation patterns
* Integrate pattern matching using regular expressions
* Connect with external APIs for dynamic responses
* Implement GUI using Tkinter
* Add voice-based interaction

## Conclusion

This project provides a beginner-friendly introduction to chatbot development. It demonstrates how predefined rules can be used to create simple conversational agents and serves as a foundation for more advanced AI-powered chatbots.

