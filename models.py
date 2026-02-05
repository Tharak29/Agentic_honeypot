from pydantic import BaseModel, Field
from typing import Optional, List, Any


class Message(BaseModel):
    sender: str
    text: str
    timestamp: Optional[str] = None


class HoneypotRequest(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: Optional[List[Any]] = Field(default_factory=list)
    metadata: Optional[Any] = None

    class Config:
        extra = "allow"   # 🚨 CRITICAL FOR GUVI


class HoneypotReply(BaseModel):
    status: str
    reply: str
