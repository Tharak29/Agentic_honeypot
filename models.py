from pydantic import BaseModel
from typing import List, Dict

class HoneypotRequest(BaseModel):
    message: str

class HoneypotResponse(BaseModel):
    is_scam: bool
    scam_type: str
    extracted_entities: Dict[str, List[str]]
    conversation: List[str]
    risk_score: float
