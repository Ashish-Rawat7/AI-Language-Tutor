import os
import re
import asyncio
import tempfile

ENABLE_TTS = os.getenv("ENABLE_TTS", "False").lower() == "true"

USE_TTS = False
try:
    import edge_tts
    USE_TTS = True
except Exception as e:
    print("Edge TTS not available:", str(e))
    USE_TTS = False


# 🔹 Clean text for natural speech
def clean_text(text: str) -> str:
    if not text:
        return ""

    # Remove markdown symbols (*, #, `, etc.)
    text = re.sub(r"[*_#`]", "", text)

    # Remove numbering (1. 2. etc.)
    text = re.sub(r"\d+\.\s*", "", text)

    # Remove extra special characters but keep punctuation for pauses
    text = re.sub(r"[^\w\s.,!?]", "", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# 🔹 Async TTS generator
async def _generate_audio_async(text: str) -> str:
    voice = "en-US-AriaNeural"  # natural female voice (change if needed)

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate="+0%",       # speed control
        pitch="+0Hz"      # tone control
    )

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    await communicate.save(temp_file.name)

    return temp_file.name


# 🔹 Public function (safe for Streamlit)
def generate_audio(text: str):
    if not ENABLE_TTS or not USE_TTS:
        return None

    try:
        cleaned_text = clean_text(text)

        if not cleaned_text:
            return None

        # Run async safely
        return asyncio.run(_generate_audio_async(cleaned_text))

    except Exception as e:
        print("TTS error:", str(e))
        return None