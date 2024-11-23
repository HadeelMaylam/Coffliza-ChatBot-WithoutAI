import streamlit as st
from streamlit_chat import message
import re
import random

# Define Eliza chatbot rules
eliza_rules = [
    (r"(who are you(.*))", ["Why are you curious?"]),
    (r"(hi|helo|hello|hey)", [
        "Hello! How are you today?",
        "Hi there! What’s on your mind?",
        "Hey! How can I help you?"
    ]),
    (r"how are you(.*)", [
        "I'm doing well! How about you?",
        "Why do you ask?"
    ]),
    (r"what is (a|an) (.*) coffee", [
        "A {1} coffee is a popular drink. Why do you ask?",
        "That’s an interesting choice! A {1} coffee is delightful. Would you like to know more?",
        "Ah, {1} coffee! Are you a fan?"
    ]),
    (r"how to make (.*)", [
        "Making {0} is a process! Do you prefer easy methods or something more elaborate?",
        "To make {0}, you’ll need the right tools. Are you ready to dive in?",
        "What makes you want to learn about making {0}?",
        "It's a secret!"
    ]),
    (r"(.*) coffee types", [
        "There are so many! What’s your favorite so far?",
        "Espresso, latte, cold brew... What type catches your eye?",
        "What’s your go-to coffee type? Let’s explore it!"
    ]),
    (r"what is your favorite coffee", [
        "I’d say espresso—it’s bold and strong, just like me.",
        "Great question! What’s your favorite?"
    ]),
    (r"(.*) caffeine(.*)", [
        "Caffeine is fascinating! Are you looking for a high-energy boost?",
        "Too much caffeine or not enough? What’s your experience with it?",
        "Let’s talk about caffeine. Are you a fan of strong coffee?"
    ]),
    (r"why do you (.*)", [
        "Why do YOU think I {0}?",
        "Interesting question—why does it matter to you?",
        "Hmmm, what makes you curious about that?"
    ]),
    (r"((.*) recommend (.*)|recommend)", [
        "I’d recommend trying a flat white if you like creamy coffee.",
        "How about a nitro cold brew? It’s unique and energizing!",
        "What about trying something new, like an affogato? It’s espresso with ice cream!"
    ])
]

# Fallback responses
eliza_rules2 = [
    "That’s intriguing. Tell me more.",
    "Why do you feel that way?",
    "I recommend you to have a cup of coffee.",
    "Hmmm, interesting. Could you elaborate?",
    "Let’s explore that thought further. What do you mean?",
    "How does that connect to coffee?"
]

# Preprocess user input
def preprocess_input(user_input):
    preprocessed = re.sub(r'[^a-zA-Z0-9\s]', '', user_input)
    return preprocessed.strip().lower()

# Generate Eliza's response
def eliza_response(user_input):
    user_input = preprocess_input(user_input)
    for pattern, responses in eliza_rules:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            return random.choice(responses).format(*match.groups())
    return random.choice(eliza_rules2)

# Streamlit app with Eliza
st.title("☕ Coffliza Chatbot")
st.write("Welcome! I'm Eliza, your coffee chatbot. Let's chat about coffee or anything on your mind.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    message(msg["content"], is_user=(msg["role"] == "user"))

# Add input at the bottom
if user_input := st.chat_input("Ask me about coffee!"):
    # Save user message in chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    message(user_input, is_user=True)
    
    # Generate and display bot response
    bot_response = eliza_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": bot_response})
    message(bot_response)
