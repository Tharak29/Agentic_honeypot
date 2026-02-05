def detect_scam(text: str) -> bool:
    keywords = [
        "account blocked",
        "verify",
        "urgent",
        "upi",
        "bank",
        "suspended"
    ]
    text = text.lower()
    return any(k in text for k in keywords)
