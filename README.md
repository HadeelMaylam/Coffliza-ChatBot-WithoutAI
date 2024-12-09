### README: Coffliza - Chatbot Powered by Regular Expressions  

**Project Name**: Coffliza  

**Description**:  
Coffliza is a chatbot built entirely using **regular expressions** (RegEx) without the use of artificial intelligence. It simulates the persona of a 43-year-old Italian barista and engages users in a simulated HR interview. This project aims to demonstrate how a rule-based approach can create an interactive chatbot experience while highlighting the challenges of building conversational systems without AI.

---

### Challenge:  
The primary challenge of this project was creating a chatbot that could simulate human-like interactions **without relying on AI models or machine learning**. By solely depending on RegEx, the bot needed to:  
1. Understand and respond to diverse user inputs.  
2. Maintain a dynamic and engaging persona.  
3. Handle unexpected inputs gracefully.  

This required carefully crafting patterns and fallback mechanisms to cover a wide range of possible user queries, all while keeping the interaction simple and intuitive.

---

### Features:
1. **Pattern-Based Chatbot**:  
   - Uses regular expressions to process and respond to user input.  
   - Matches specific patterns to predefined responses.  

2. **Dynamic Persona**:  
   - Represents Coffliza, a barista with a rich professional background in Italian coffee culture.  

3. **Fallback Handling**:  
   - Provides generic responses for inputs that do not match defined patterns.  

4. **Team Collaboration**:  
   - Developed by a team of four, each contributing to different aspects of the project.

---

### Files Included:
1. **Talk_to_Coffliza.py**:  
   The main chatbot logic and interface, built with Streamlit.  
   - Handles user inputs using RegEx.  
   - Responds dynamically to user queries.  
   - Implements a fallback system for unmatched inputs.

2. **Team.py**:  
   Provides an overview of the team and project description.  

3. **Coffliza_CV.py**:  
   Displays Coffliza’s professional CV, highlighting her skills and achievements.  

4. **requirements.txt**:  
   Contains the dependencies required for the project.  

5. **eliza.jpg**:  
   A visual representation of Coffliza used in the CV.

---

### Installation:
1. Clone the repository:  
   ```bash
   git clone <repository_url>
   cd coffliza
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the chatbot:  
   ```bash
   streamlit run Talk_to_Coffliza.py
   ```

4. Access Coffliza’s CV:  
   ```bash
   streamlit run Coffliza_CV.py
   ```

5. Explore the team page:  
   ```bash
   streamlit run Team.py
   ```

---

### Usage:
- Launch the chatbot and interact with Coffliza by typing questions or statements.  
- Use the CV page to explore Coffliza’s professional background.  
- Check the team page to learn about the contributors.  

---

### Team Members:
- **Alawi**: Brainstorming, main page, team page, Git/GitHub management.  
- **Ibrahim**: Brainstorming, main page, team page, Git/GitHub management.  
- **Hadeel**: Brainstorming, chat page, bot development using regular expressions.  
- **Shaden**: Brainstorming, chat page, bot development using regular expressions.  

---

### License:
This project is for educational and experimental purposes. Redistribution and modification are permitted with proper attribution to the authors.  

---

**Note**:  
Coffliza is not powered by AI. Its behavior is entirely driven by pattern-matching logic, which makes it a unique experiment in building interactive chatbots using fundamental programming techniques.
