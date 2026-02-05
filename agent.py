class HoneypotAgent:
    def generate_reply(self, history):
        if not history:
            return "Why is my account being blocked?"

        return "I already told you I am confused. Can you explain again?"
