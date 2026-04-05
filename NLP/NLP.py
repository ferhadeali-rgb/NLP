
import re
import random

# Predefined responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "how_are_you": ["I'm just a bot, but I'm doing great!", "All good here!"],
    "name": ["I'm IntelliChat, your assistant."],
    "help": ["I can chat with you! Try saying hello, ask my name, or say bye."]
}

# Intent patterns
patterns = {
    "greeting": r"\b(hello|hi|hey)\b",
    "goodbye": r"\b(bye|goodbye|see you)\b",
    "how_are_you": r"\b(how are you)\b",
    "name": r"\b(your name|who are you)\b",
    "help": r"\b(help|what can you do)\b"
}

def preprocess(text):
    return text.lower()

def detect_intent(user_input):
    for intent, pattern in patterns.items():
        if re.search(pattern, user_input):
            return intent
    return "unknown"

def chatbot():
    print("🤖 IntelliChat: Hello! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("🤖 IntelliChat: Goodbye!")
            break
        
        user_input = preprocess(user_input)
        intent = detect_intent(user_input)
        
        if intent in responses:
            print("🤖 IntelliChat:", random.choice(responses[intent]))
        else:
            print("🤖 IntelliChat: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()