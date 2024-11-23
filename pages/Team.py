import streamlit as st

# Team members and their roles
team_members = [
    {'name': 'Alawi', 'roles': "Brainstorm Ideas , Main Page , Team Page , Git/Github"},
    {'name': 'Ibrahim', 'roles': "Brainstorm Ideas , Main Page , Team Page , Git/Github"},
    {'name': 'Hadeel', 'roles': "Brainstorm Ideas ,Chat Page , Developing the bot using Regular Expressions "},
    {'name': 'Shaden', 'roles': "Brainstorm Ideas ,Chat Page , Developing the bot using Regular Expressions "}
]

# Project description
project_description = """
**Coffliza: Your AI-Powered Chat Companion**

We are four students who have worked on a simple chatbot that takes on the character
of a 43-year-old Italian woman working as a barista. She is applying to a company,
and our project consists of an interview conducted by the user as an HR representative
with Coffliza. The project's goal is to experiment with how long it takes a person to
recognize whether they are interacting with a bot or not.
"""

# Create a title
st.title("Team Coffliza")

# Create a table
st.table(team_members)

# Add the project description
st.markdown(project_description)