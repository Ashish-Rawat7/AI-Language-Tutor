#  AI Language Tutor  
### Learn Languages Smarter with AI-Powered Conversations

---

##  Overview

**AI Language Tutor** is an intelligent language learning application that helps users improve their communication skills through interactive conversations, real-time grammar correction, and personalized feedback.

The system leverages modern AI models to simulate a human-like tutor, enabling learners to practice languages in a natural and engaging way — from beginner to advanced levels.

---

##  Features

-  **Conversational Practice** — Chat with an AI tutor in real-time  
-  **Grammar Correction** — Instant feedback and corrections  
-  **Vocabulary Enhancement** — Learn new words with contextual examples  
-  **Structured Learning** — Guided responses with explanations  
-  **Multi-language Support** — Switch between languages easily  
-  **Text-to-Speech (TTS)** — Hear responses (optional)  
-  **Speech-to-Text (STT)** — Voice input support (optional)  
-  **Adaptive Learning** — Responses tailored to user input  

---

## 🛠️ Tech Stack

**Frontend**
- Streamlit (UI Framework)

**Backend**
- Python

**AI / NLP**
- Google Gemini API (`google-genai`)
- LanguageTool  for Grammar Checking

**Utilities**
- python-dotenv (Environment Management)
- gTTS (Text-to-Speech)
- SpeechRecognition (Speech-to-Text)

---

## Live Demo
https://ai-language-tutor-ashish.streamlit.app/

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-language-tutor.git
cd ai-language-tutor

## Steps you need to Follow after the clone

### Step 1
### Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

### Step 2
### Install Dependencies
pip install -r requirements.txt

### Step 3
### Setup Environment Variables
Create a .env file in the root directory:

GEMINI_API_KEY=your_api_key_here           
GEMINI_MODEL=models/gemini-2.0-flash      

DEFAULT_LANGUAGE=en
ENABLE_TTS=True
ENABLE_STT=False
DEBUG=True


### Step 4
Run the Application

streamlit run app.py


## Usage Guide
Open the app in your browser (http://localhost:8501)
Enter a sentence or question in your target language
Receive:
  Corrected sentence
  Explanation
  Better alternatives
  Vocabulary tips
  Follow-up questions
Continue the conversation to improve fluency


## AI Model Details
Primary Model: Google Gemini (models/gemini-2.0-flash)
Purpose: Text generation for tutoring and feedback
Capabilities:
Grammar correction
Natural conversation
Contextual explanations

##Future Improvements
🧠 User progress tracking dashboard
📊 Difficulty-based adaptive learning system
🌍 More language support
🗣️ Advanced voice interaction (real-time speech)
💾 Cloud database integration
🎨 Enhanced UI (ChatGPT-style interface)
🔄 Multi-model fallback (Gemini + OpenAI)

## Contributing

### Contributions are welcome!

Steps:
Fork the repository
Create a new branch (feature/your-feature)
Commit your changes
Push to your fork
Create a Pull Request


## License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute.


##  Support

If you found this project useful, consider giving it a ⭐ on GitHub!