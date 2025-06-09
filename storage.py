import os
import json

class UserCollection:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def get_user_file(self, user_id):
        return os.path.join(self.data_dir, f"{user_id}.json")

    def get_collection(self, user_id):
        file = self.get_user_file(user_id)
        if os.path.exists(file):
            with open(file, "r") as f:
                return json.load(f)
        return []

    def add_card(self, user_id, card):
        collection = self.get_collection(user_id)
        collection.append(card['name'])
        with open(self.get_user_file(user_id), "w") as f:
            json.dump(collection, f)