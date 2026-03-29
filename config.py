import os
from dotenv import load_dotenv

load_dotenv()


def get_env(key, default=None, required=False):
    value = os.getenv(key, default)
    if required and not value:
        raise RuntimeError(f"{key} is required")
    return value


def to_bool(val):
    return str(val).lower() in ["true", "1", "yes"]

GEMINI_API_KEY = get_env("GEMINI_API_KEY", required=True)
GEMINI_MODEL = get_env("GEMINI_MODEL", "models/gemini-2.0-flash")

DEFAULT_LANGUAGE = get_env("DEFAULT_LANGUAGE", "en")

ENABLE_TTS = to_bool(get_env("ENABLE_TTS", "False"))
ENABLE_STT = to_bool(get_env("ENABLE_STT", "False"))

DEBUG = to_bool(get_env("DEBUG", "True"))