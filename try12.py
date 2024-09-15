import nltk
from nltk.chat.util import Chat, reflections
import re

responses = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hi there! What can I do for you?']),
    (r'what is your name?', ['I am a chatbot created by Badsha.', 'You can call me Chatbot.']),
    (r'how are you?', ['I am  a AI intraction tool, but I am good. How about you?', 'I am good, thank you for asking!']),
    (r'quit|bye|exit', ['Goodbye! Have a great day!', 'Bye! Take care.']),
    (r'(.*)', ['Sorry, I do not understand that.', 'Can you please rephrase that?'])
]

chatbot = Chat(responses, reflections)

def bot():
    print("Hello! I am a chatbot. Type 'quit', 'bye', or 'exit' to end the chat.")
    while True:
        user = input("You: ")
        if re.match(r'quit|bye|exit', user, re.I):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    bot()
