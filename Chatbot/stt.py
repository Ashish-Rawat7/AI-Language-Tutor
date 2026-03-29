import os

ENABLE_STT = os.getenv("ENABLE_STT", "False").lower() == "true"

USE_STT = False

if ENABLE_STT:
    try:
        import whisper
        model = whisper.load_model("base")
        USE_STT = True
    except Exception as e:
        print("STT disabled:", str(e))
        USE_STT = False
else:
    print("STT disabled via config")


def transcribe_audio(audio_file):
    if not USE_STT:
        return ""

    try:
        result = model.transcribe(audio_file)
        return result["text"]
    except Exception as e:
        print("STT error:", str(e))
        return ""