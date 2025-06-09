import os
import json
import random

DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)

def get_user_file(user_id):
    return os.path.join(DATA_PATH, f"{user_id}.json")

def give_random_card(user_id):
    card = {
        "name": random.choice(["Синя качка", "Червона качка", "Зелена качка"]),
        "level": random.randint(1, 5),
        "image_path": "attached_assets/duck.jpg"
    }
    user_file = get_user_file(user_id)
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            collection = json.load(f)
    else:
        collection = []

    collection.append(card)
    with open(user_file, "w") as f:
        json.dump(collection, f)

    return card

def get_user_collection(user_id):
    user_file = get_user_file(user_id)
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            return json.load(f)
    return []
