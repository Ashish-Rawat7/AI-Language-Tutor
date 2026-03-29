import json
import os

DATA_PATH = "data/user_data.json"
MAX_HISTORY = 20  


def load_data():
    if not os.path.exists(DATA_PATH):
        return {"history": [], "vocab": []}

    try:
        with open(DATA_PATH, "r") as f:
            content = f.read().strip()
            if not content:
                return {"history": [], "vocab": []}
            return json.loads(content)
    except Exception:
        return {"history": [], "vocab": []}


def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)


def update_progress(user_input, response, difficulty, vocab):
    data = load_data()

    # 🔹 Add new entry
    data["history"].append({
        "user": user_input,
        "response": response,
        "difficulty": difficulty
    })

    data["history"] = data["history"][-MAX_HISTORY:]

    data["vocab"].extend(vocab)
    data["vocab"] = list(set(data["vocab"]))

    save_data(data)

def reset_data():
    save_data({"history": [], "vocab": []})