from pydantic import BaseModel
from typing import Optional


class InterviewResponse(BaseModel):
    reply: str
    score: Optional[float] = None
    feedback: Optional[str] = None
    question_number: Optional[int] = None
    curriculum_day: Optional[int] = None
    done: bool
    final_evaluation: Optional[str] = None