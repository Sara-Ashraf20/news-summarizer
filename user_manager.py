import os
import json

DATA_FILE = "data/user_data.json"

class UserManager:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump({"preferences": [], "history": []}, f)
        self.load_data()

    def load_data(self):
        with open(DATA_FILE, "r") as f:
            self.data = json.load(f)

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.data, f, indent=2)

    def add_preference(self, topic):
        if topic not in self.data["preferences"]:
            self.data["preferences"].append(topic)
            self.save_data()

    def log_search(self, topic, summary):
        self.data["history"].append({"topic": topic, "summary": summary})
        self.save_data()

    def get_preferences(self):
        return self.data["preferences"]

    def get_history(self):
        return self.data["history"]
