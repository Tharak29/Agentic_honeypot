class HoneypotAgent:
    def generate_reply(self, history: list) -> str:
        replies = [
            "Why is my account being blocked?",
            "I don’t understand, can you explain?",
            "Is this really from the bank?",
            "What happens if I don’t verify now?",
            "Can you send details again?"
        ]
        return replies[len(history) % len(replies)]
