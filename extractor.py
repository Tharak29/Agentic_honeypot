import re

def extract_intelligence(text: str, store: dict):
    store["upiIds"] += re.findall(r"\b[\w.-]+@upi\b", text)
    store["bankAccounts"] += re.findall(r"\b\d{9,18}\b", text)
    store["phishingLinks"] += re.findall(r"https?://\S+", text)
    store["phoneNumbers"] += re.findall(r"\+91\d{10}", text)

    for kw in ["urgent", "verify", "blocked", "suspended"]:
        if kw in text.lower() and kw not in store["suspiciousKeywords"]:
            store["suspiciousKeywords"].append(kw)
