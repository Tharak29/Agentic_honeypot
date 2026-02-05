from fastapi import FastAPI, Header, HTTPException
from models import HoneypotRequest, HoneypotReply
from detector import detect_scam
from extractor import extract_intelligence
from agent import HoneypotAgent
from callback import send_final_callback

app = FastAPI(title="Agentic Honeypot API")

API_KEY = "GUVI123"

SESSIONS = {}


@app.post("/message", response_model=HoneypotReply)
def honeypot(req: HoneypotRequest, x_api_key: str | None = Header(None)):

    # TEMPORARILY LENIENT FOR GUVI
    if x_api_key and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    sid = req.sessionId

    if sid not in SESSIONS:
        SESSIONS[sid] = {
            "scamDetected": False,
            "messages": 0,
            "intelligence": {
                "bankAccounts": [],
                "upiIds": [],
                "phishingLinks": [],
                "phoneNumbers": [],
                "suspiciousKeywords": []
            }
        }

    session = SESSIONS[sid]
    session["messages"] += 1

    # Scam detection
    if detect_scam(req.message.text):
        session["scamDetected"] = True

    # Intelligence extraction
    extract_intelligence(req.message.text, session["intelligence"])

    # Agent reply
    agent = HoneypotAgent()
    reply_text = agent.generate_reply(req.conversationHistory)

    # FINAL GUVI CALLBACK
    if session["scamDetected"] and session["messages"] >= 5:
        payload = {
            "sessionId": sid,
            "scamDetected": True,
            "totalMessagesExchanged": session["messages"],
            "extractedIntelligence": session["intelligence"],
            "agentNotes": "Urgency-based financial impersonation scam"
        }
        send_final_callback(payload)

    return {
        "status": "success",
        "reply": reply_text
    }
