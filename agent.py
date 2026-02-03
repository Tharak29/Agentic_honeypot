import requests
from extractor import extract_entities

SCAMMER_API = "http://127.0.0.1:9000/scammer/respond"

class HoneypotAgent:
    def __init__(self):
        self.history = []
        self.entities = {
            "upi_ids": [],
            "bank_accounts": [],
            "phishing_links": []
        }

    def persona_message(self, step: int):
        personas = [
            "Hello, I got a message about my account",
            "I am confused, what should I do?",
            "Can you explain again?",
            "Is this really from the bank?",
            "How do I complete verification?"
        ]
        return personas[step % len(personas)]

    def run(self, rounds: int = 5):
        user_message = "Hi"
        for i in range(rounds):
            response = requests.post(
                SCAMMER_API,
                params={"message": user_message}
            )
            scammer_reply = response.json()["reply"]
            self.history.append(scammer_reply)

            extracted = extract_entities(scammer_reply)
            for key in self.entities:
                self.entities[key].extend(extracted[key])

            user_message = self.persona_message(i)
