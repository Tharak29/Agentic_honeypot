from fastapi import FastAPI
import random

app = FastAPI(title="Mock Scammer API")

SCAM_SCRIPT = [
    "I am calling from bank support",
    "Your account has suspicious activity",
    "Please send Rs 10 to verify",
    "Use this UPI ID: verify@upi",
    "Click here to confirm: http://fake-bank-login.com",
    "My bank account number is 9876543210"
]

@app.post("/scammer/respond")
def scammer_response(message: str):
    return {"reply": random.choice(SCAM_SCRIPT)}
