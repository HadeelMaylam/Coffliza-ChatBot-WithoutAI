
import streamlit as st
from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right

user_input = st.text_input("Enter your message:")
st.button("Send")



import re
import random # used to randomize the responses

# Expected questions
eliza_rules = [
    (r"(who are you (.*))", ["why are you curios?"]),

    (r"(hi|helo|heloo|hello|hey)", [
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
        "It's a secret"
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
    ]),
    ((r"((.*) coffe|coffeee|cofee|coffie (.*)|coffee)"), [
        "Let’s talk about coffee. What would you like to know?",
        "Coffee is fascinating! Do you have a favorite type?",
        "What’s your relationship with coffee—love, hate, or something in between?"
    ]),
    (r"((.*) espresso|expresso (.*)| espresso | expresso)", [
        "Espresso is a great base for many drinks. What’s your favorite espresso-based coffee?",
        "Let’s talk espresso! Do you take it straight, or mix it with milk?",
        "Espresso is powerful! Do you like it strong or sweetened?"
     ]),
    (r"((.*) caffeine|caffine|cafeen (.*)|caffeine)" , ["Let's talk caffeine. Are you a fan of strong coffee?",
    "Are you thinking about caffeine levels in your drink, or just curious?",
    "Caffeine is such a hot topic! What's your personal take on it?"]),
]


# Random unexpected questions
# (.*)
eliza_rules2=[
        "That’s intriguing. Tell me more.",
        "Why do you feel that way?",
        "I recommend you to have a cup of coffee ",
        "Hmmm, interesting. Could you elaborate?",
        "Let’s explore that thought further. What do you mean?",
        "How does that connect to coffee?"
    ]


def eliza_response(user_input):
    # First rule set
    #add button to quit
     
    while user_input.lower() != "quit":
      for pattern, responses in eliza_rules: # iterate over the rule set to find the pattern
          match = re.match(pattern, user_input, re.IGNORECASE)
          if match:
              return random.choice(responses).format(*match.groups()) #response from eliza_rules

      return random.choice(eliza_rules2) #response from eliza_rules2, for unexpected questions






def eliza_chatbot():
    print("ELIZA: Hello! I'm here to chat with you. (Type 'quit' to exit)")

    while True: #loop to keep the conversation
        user_input = input("You: ")
        if user_input.lower() == "quit": #keyword to stop the conversation
            print("ELIZA: Goodbye! It was nice chatting with you.")
            break
        response = eliza_response(user_input) #call eliza_response
        print(f"ELIZA: {response}")

# Run the chatbot
if __name__ == "__main__":
    eliza_chatbot()