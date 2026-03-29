import re

def extract_vocab(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = list(set(words))
    return unique_words[:5]  