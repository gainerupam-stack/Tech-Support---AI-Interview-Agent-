from pydantic import BaseModel
from typing import Optional


class Member(BaseModel):
    id: str


class Candidate(BaseModel):
    member: Member


class InterviewRequest(BaseModel):
    sessionId: str
    candidate: Optional[Candidate] = None
    message: Optional[str] = None