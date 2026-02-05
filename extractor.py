import re


def extract_intelligence(text: str, store: dict):
    upi = re.findall(r"\b[\w.\-]+@upi\b", text)
    phone = re.findall(r"\b\d{10}\b", text)
    links = re.findall(r"https?://\S+", text)

    for u in upi:
        if u not in store["upiIds"]:
            store["upiIds"].append(u)

    for p in phone:
        if p not in store["phoneNumbers"]:
            store["phoneNumbers"].append(p)

    for l in links:
        if l not in store["phishingLinks"]:
            store["phishingLinks"].append(l)

    keywords = ["urgent", "verify", "blocked", "suspended"]
    for k in keywords:
        if k in text.lower() and k not in store["suspiciousKeywords"]:
            store["suspiciousKeywords"].append(k)
