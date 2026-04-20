import os

ENABLE_GRAMMAR = os.getenv("ENABLE_GRAMMAR", "True").lower() == "true"

USE_GRAMMAR = False

if ENABLE_GRAMMAR:
    try:
        import language_tool_python
        tool = language_tool_python.LanguageTool('en-US')
        USE_GRAMMAR = True
    except Exception as e:
        print("Grammar tool failed:", str(e))
        USE_GRAMMAR = False
else:
    print("Grammar disabled via config")


def correct_grammar(text):
    if not USE_GRAMMAR:
        return text, []

    matches = tool.check(text)

    corrected_text = language_tool_python.utils.correct(text, matches)

    explanations = []
    for match in matches:
        explanations.append({
            "message": match.message,
            "suggestions": match.replacements
        })

    return corrected_text, explanations