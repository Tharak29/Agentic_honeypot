# Agentic Honeypot API – GUVI Hackathon

## Authentication
This API requires an API key.

Header:
x-api-key: GUVI_SECRET_123

## Endpoint
POST /honeypot/analyze

## Request Body
{
  "message": "Your bank account needs verification"
}

## How to Run

1. Install dependencies
pip install -r requirements.txt

2. Start Mock Scammer API
uvicorn mock_scammer_api:app --port 9000

3. Start Honeypot API
uvicorn app:app --reload

4. Test via Swagger
http://127.0.0.1:8000/docs
