### README: Coffliza - An AI-Powered Chatbot

**Project Name**: Coffliza

**Description**:  
Coffliza is an AI-powered chatbot designed to simulate the persona of a 43-year-old Italian barista applying for a job. The bot interacts with users in a simulated HR interview format, allowing them to evaluate Coffliza's responses and personality. The project explores how users engage with AI systems and aims to assess the time it takes to identify the bot as non-human.

---

### Features:
1. **Interactive Chatbot**:
   - Built with Streamlit for a simple and intuitive interface.
   - Uses regular expressions to match user inputs and generate relevant responses.

2. **Dynamic Personality**:
   - Represents Coffliza, a barista from Verona, Italy, with over 15 years of coffee expertise.
   - Capable of discussing topics like coffee brewing, career experiences, and Italian culture.

3. **User Experience**:
   - Chat interface allows users to ask questions and receive tailored responses.
   - Includes fallback responses to handle unrecognized queries gracefully.

4. **Team Contribution**:
   - Developed by a team of four, with collaborative efforts in brainstorming, interface design, and bot development using regular expressions.

---

### Files Included:
1. **Talk_to_Coffliza.py**:  
   Contains the main chatbot logic and interface implementation.  
   Key Features:  
   - Chat rules using regular expressions.  
   - Dynamic responses and fallback handling.  
   - User-friendly Streamlit interface.

2. **Team.py**:  
   Provides an overview of the project and introduces the team members involved in its development.  
   Key Features:  
   - Project description and purpose.  
   - Team member roles and contributions.

3. **Coffliza_CV.py**:  
   Displays Coffliza's professional CV in a visually appealing format using Streamlit.  
   Key Features:  
   - Contact details, skills, experience, education, and achievements.  
   - A personalized image representing Coffliza.

4. **requirements.txt**:  
   Lists the Python dependencies required to run the project.  
   Key Libraries:  
   - `streamlit` (1.27.0): For building the web interface.  
   - `streamlit-chat` (0.0.2): For integrating the chat feature.

5. **eliza.jpg**:  
   A visual representation of Coffliza used in the CV display.

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

4. Access Coffliza's CV:
   ```bash
   streamlit run Coffliza_CV.py
   ```

5. Explore the team information:
   ```bash
   streamlit run Team.py
   ```

---

### Usage:
- Launch the chatbot and interact with Coffliza by typing questions or statements.
- Use the CV and team pages to learn more about Coffliza's background and the project team.
- Evaluate how long it takes to determine whether Coffliza is an AI bot.

---

### Authors:
- **Alawi**: Brainstorming, main page, team page, Git/GitHub management.
- **Ibrahim**: Brainstorming, main page, team page, Git/GitHub management.
- **Hadeel**: Brainstorming, chat page, bot development using regular expressions.
- **Shaden**: Brainstorming, chat page, bot development using regular expressions.

---

### License:
This project is for educational and experimental purposes. Redistribution and modification are permitted with proper attribution to the authors. 

Enjoy chatting with Coffliza and exploring the art of conversational AI!
