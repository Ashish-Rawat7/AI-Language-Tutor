import streamlit as st
from Chatbot.agent import generate_response
from Chatbot.grammar import correct_grammar
from Chatbot.difficulty import calculate_difficulty
from Chatbot.vocab import extract_vocab
from Chatbot.tts import generate_audio
from Chatbot.stt import transcribe_audio
from Chatbot.memory import update_progress, load_data, reset_data


st.set_page_config(page_title="AI Language Tutor", layout="centered")

st.title("AI Language Learning Agent")

language = st.selectbox(
    "Select Language",
    ["English", "Spanish", "French", "German", "Hindi"]
)

audio_input = st.file_uploader("Upload speech (optional)", type=["wav", "mp3"])

user_input = ""

if audio_input:
    user_input = transcribe_audio(audio_input)

    if user_input:
        st.info(f"Transcribed: {user_input}")
    else:
        st.warning("Speech-to-text not available")
    st.info(f"Transcribed: {user_input}")

text_input = st.text_input("Or type your sentence:")

if text_input:
    user_input = text_input

if st.button("Send"):

    if user_input:

        corrected, explanations = correct_grammar(user_input)

        if user_input != corrected:
            st.warning(f"Correction: {corrected}")

            for exp in explanations:
                st.write(f"🔹 {exp['message']}")
                if exp["suggestions"]:
                    st.write(f"Suggestions: {exp['suggestions']}")

        response = generate_response(corrected, language)

        difficulty = calculate_difficulty(user_input)

        vocab = extract_vocab(user_input)

        st.markdown("### 🤖 Tutor")
        st.markdown(response)
        st.info(f"Difficulty Level: {difficulty}")

        st.write("Vocabulary:")
        for word in vocab:
            st.write(f"- {word}")

        audio_file = generate_audio(response)
        st.audio(audio_file)

        update_progress(user_input, response, difficulty, vocab)

with st.sidebar:
    st.header("Controls")
    if st.button("Clear History"):
        reset_data()
        st.success("History cleared!")

    st.divider()

    st.header("Progress")

    data = load_data()

    st.write(f"Conversations: {len(data.get('history', []))}")

    st.write("Vocabulary learned:")
    for word in data.get("vocab", [])[:20]:
        st.write(f"- {word}")