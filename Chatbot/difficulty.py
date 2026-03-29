def calculate_difficulty(text):
    words = text.split()
    length = len(words)

    if length < 5:
        return "Beginner"
    elif length < 12:
        return "Intermediate"
    else:
        return "Advanced"