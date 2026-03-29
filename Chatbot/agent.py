from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL, DEBUG

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(user_input, language="English"):
    """
    Production-ready Gemini response (new SDK)
    """

    prompt = f"""
You are a professional {language} tutor.

Respond in this format:

1. Corrected Sentence:
2. Explanation:
3. Better Alternatives:
4. Vocabulary Tip:
5. Follow-up Question:

User Input:
{user_input}
"""

    models_to_try = [
        GEMINI_MODEL,
        "models/gemini-2.0-flash-lite",
        "models/gemini-flash-lite-latest",
    ]

    last_error = None
    for model_name in models_to_try:
        try:
            if DEBUG:
              print(f"Trying model: {model_name}")

            response = client.models.generate_content(
                model=model_name,
                contents=[
                   {
                    "role": "user",
                    "parts": [{"text": prompt}],
                   }
                ],
                config={
                    "temperature": 0.5,
                    "max_output_tokens": 1024,
               },
           )

            if response and hasattr(response, "text") and response.text:
                return response.text.strip()

        except Exception as e:
            last_error = str(e)  
            print(f"🔥 ERROR ({model_name}):", last_error)
            continue

    return f"FINAL ERROR: {last_error}"