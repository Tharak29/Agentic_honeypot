import requests


def send_final_callback(payload: dict):
    try:
        requests.post(
            "https://hackathon.guvi.in/api/updateHoneyPotFinalResult",
            json=payload,
            timeout=5
        )
    except Exception as e:
        print("Callback failed:", e)
