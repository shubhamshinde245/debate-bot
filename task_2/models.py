# --- Models ---
from pydantic import BaseModel


class ChatRequest(BaseModel):
    conversation_id: str | None = None
    message: str
    topic: str | None = None
    side: str | None = None


class Message(BaseModel):
    role: str
    message: str


class ChatResponse(BaseModel):
    conversation_id: str
    message: list[Message]
