import streamlit as st
from streamlit_chat import message
import re
import random

# Define Eliza chatbot rules
eliza_rules = [
    # Greetings
    (r".*\b(hi|hello|hey|ciao|)\b.*", [
        "Hello! Thank you for having me. I’m excited to discuss this opportunity.",
        "Hi there! It’s great to meet you. Let’s talk coffee and careers!",
        "Hello! I’m looking forward to learning more about this role."
    ]),

    # Name Inquiry
    (r".*\b(what is your name|who are you)\b.*", [
        "My name is Coffliza, nice to meet you! What’s yours?",
        "I’m Coffliza, a passionate barista and coffee consultant. What about you?",
        "I’m Coffliza! Let’s talk coffee."
    ]),

    # Age Inquiry
    (r".*\b(how old are you|your age)\b.*", [
        "I’m 43 years old, and I’ve spent over 15 of those years mastering the art of coffee.",
        "I’m 43, and coffee has been my passion for most of my life.",
        "I’m 43! I started my coffee journey in my early twenties."
    ]),

    # Location Inquiry
    (r".*\b(where do you live|your location|where are you from)\b.*", [
        "I live in Verona, Italy—a city with a rich coffee culture.",
        "I’m based in Verona, Italy, where coffee is a way of life.",
        "Verona, Italy is my home. Have you ever visited?"
    ]),

    # Background and Experience
    (r".*\b(about yourself|background|who are you)\b.*", [
        "I’m Coffliza, a barista and coffee consultant with over 15 years of experience in Italian coffee culture.",
        "I’m a professional barista from Verona, Italy, passionate about sharing my love for coffee.",
        "I specialize in espresso, modern brewing techniques, and creating unique coffee experiences."
    ]),

    # Career Journey
    (r".*\b(cv|career|journey|experience)\b.*", [
        "Sure! My journey began as a barista at Espresso Italiano, where I honed my brewing skills. Then, I became a lead barista at Caffè Dolce Vita, managing a team and designing menus. Currently, I work as a coffee consultant, training baristas and creating personalized coffee experiences.",
        "I’d be happy to! I started as a barista, progressed to lead barista roles, and now I consult cafés and host coffee workshops globally.",
        "Of course! My career spans over 15 years, starting with hands-on experience as a barista and growing into a consultant role, sharing Italian coffee culture worldwide."
    ]),

    # Technical Skills
    (r".*\b(skills|coffee sourcing|expertise)\b.*", [
        "I specialize in espresso brewing, modern brewing techniques, and coffee bean sourcing to create unique blends.",
        "Yes, I’ve sourced beans for custom blends and worked closely with suppliers to ensure quality.",
        "My core skills include crafting recipes, mentoring teams, and sourcing beans that fit specific flavor profiles."
    ]),

    # Challenges and Strengths
    (r".*\b(challenge|complaint|problem)\b.*", [
        "Once, a customer was dissatisfied with a drink. I listened carefully, remade their coffee to their liking, and ensured they left happy. It’s all about communication and care.",
        "During a busy rush, a team member made repeated errors. I stayed calm, offered guidance, and helped manage the orders to keep things running smoothly.",
        "When a supplier delayed delivery, I quickly found a local alternative to maintain service quality. Challenges are opportunities to innovate."
    ]),

    # Growth and Development (Coffliza asks HR)
    (r".*\b(growth|development|progression)\b.*", [
        "Are there training programs or workshops for employees to grow professionally?",
        "Does the company support attending competitions or coffee events for skill enhancement?",
        "What’s the career progression path for someone in this role?"
    ]),

    # Salary and Benefits (Coffliza asks HR)
    (r".*\b(salary|benefit|perks)\b.*", [
        "Could you share the salary range for this position?",
        "What’s included in the benefits package? Are there perks like discounts or travel allowances?",
        "Is there flexibility in the salary based on additional certifications or experience?"
    ])
]


# Fallback responses
fallback_responses = [
    "I didn’t quite catch that. Could you say it another way?",
    "Hmmm, I’m not sure I understand. Can you clarify?",
    "Could you repeat that? I want to make sure I get it right.",
    "Interesting... but I might need more details to respond properly.",
    "That’s intriguing. Can you elaborate a bit more?",
    "Hmmm, could you rephrase your question?"
]

# Preprocess user input
def preprocess_input(user_input):
    preprocessed = re.sub(r"[^\w\s]", "", user_input)  # Remove non-alphanumeric characters
    return preprocessed.strip().lower()

# Generate Eliza's response
def eliza_response(user_input):
    user_input = preprocess_input(user_input)
    for pattern, responses in eliza_rules:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            return response.format(*match.groups()) if match.groups() else response
    return random.choice(fallback_responses)

# Streamlit app with Eliza
st.title("☕ Coffliza")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit app with Eliza
st.title("☕ Coffliza")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for i, msg in enumerate(st.session_state.messages):  # Use enumerate for unique keys
    message(msg["content"], is_user=(msg["role"] == "user"), key=f"message_{i}")

# Add input at the bottom
if user_input := st.chat_input("Type something to Coffliza..."):
    # Save user message in chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    message(user_input, is_user=True, key=f"user_input_{len(st.session_state.messages)}")  # Unique key for user input
    
    # Generate and display bot response
    bot_response = eliza_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": bot_response})
    message(bot_response, key=f"bot_response_{len(st.session_state.messages)}")  # Unique key for bot response





