SCAM_KEYWORDS = [
    "bank", "upi", "verify", "refund",
    "account", "click", "send", "money"
]

def detect_scam(text: str) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in SCAM_KEYWORDS)
