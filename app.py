from fastapi import FastAPI, Header, HTTPException
from detector import detect_scam
from agent import HoneypotAgent
from models import HoneypotRequest, HoneypotResponse

app = FastAPI(title="Agentic Honeypot API")

# 🔐 API KEY (change if needed)
VALID_API_KEY = "GUVI_SECRET_123"

@app.get("/")
def root():
    return {"status": "Agentic Honeypot API is running"}

@app.post("/honeypot/analyze", response_model=HoneypotResponse)
def analyze_message(
    req: HoneypotRequest,
    x_api_key: str = Header(None)
):
    # 🔐 API KEY VALIDATION
    if x_api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    # 🔍 Scam Detection
    if not detect_scam(req.message):
        return {
            "is_scam": False,
            "scam_type": "None",
            "extracted_entities": {
                "upi_ids": [],
                "bank_accounts": [],
                "phishing_links": []
            },
            "conversation": [],
            "risk_score": 0.0
        }

    # 🤖 Agentic Honeypot Execution
    agent = HoneypotAgent()
    agent.run()

    risk_score = min(1.0, 0.4 + 0.15 * len(agent.history))

    return {
        "is_scam": True,
        "scam_type": "Bank / UPI Scam",
        "extracted_entities": agent.entities,
        "conversation": agent.history,
        "risk_score": round(risk_score, 2)
    }
