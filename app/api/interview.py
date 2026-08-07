from fastapi import APIRouter
from models.request import InterviewRequest

router = APIRouter()

@router.post("/api/interview")
def interview(request: InterviewRequest):

    return {
        "reply": "Welcome. Let's begin your interview.",
        "done": False
    }