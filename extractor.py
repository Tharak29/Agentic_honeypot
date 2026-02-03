import re

def extract_entities(text: str):
    return {
        "upi_ids": re.findall(r"\b[\w.-]+@upi\b", text),
        "bank_accounts": re.findall(r"\b\d{9,18}\b", text),
        "phishing_links": re.findall(r"https?://\S+", text)
    }
