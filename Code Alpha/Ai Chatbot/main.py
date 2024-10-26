import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have the necessary NLTK data files
nltk.download('punkt')

# Define a list of patterns and responses
pairs = [
    [ 
        r"my name is Ai Chatbot",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello! How can I assist you today?",]
    ], 
    [
        r"how are you?",
        ["I'm just a bunch of code, but thanks for asking!",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm not sure where you are located. Can you tell me?",]
    ],
    [
        r"what is your name?",
        ["I am an ai chatbot created to assist you.",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but thanks for asking! How can I help you?",]
    ],
    [
        r"what can you do?",
        ["I can answer your questions, chat with you, and help with information you need.",]
    ],
    [
        r"tell me a joke",
        ["Why did the scarecrow win an award? Because he was outstanding in his field!",]
    ],
    [
        r"what's the weather like?",
        ["I can't check the weather right now, but you can look it up online!",]
    ],
    [
        r"i need some help|assist|support",
        ["Sure! What do you need help with?",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! If you have any more questions, feel free to ask.",]
    ],
    [
        r"what is your favorite color?",
        ["I don’t have preferences, but blue is a popular choice among many!",]
    ],
    [
        r"where are you from?",
        ["I exist in the digital realm, created to assist you!",]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that. Could you please rephrase?"]
    ]

]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Start the conversation
def start_chat():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
