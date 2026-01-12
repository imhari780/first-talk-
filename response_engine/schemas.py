from typing import List, Optional

from pydantic import BaseModel, Field


class Interaction(BaseModel):
    sender_type: str
    content: str


class ResponseEngineRequest(BaseModel):
    room_type: str
    recent_interactions: List[Interaction]
    semantic_context: Optional[List[str]] = Field(default_factory=list)


class ResponseEngineResponse(BaseModel):
    text: Optional[str] = None
    audio_tokens: Optional[List[str]] = None
