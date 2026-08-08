from fastapi import APIRouter
from app.models.request import InterviewRequest
from app.services.interview_service import process

router = APIRouter()


@router.post("/api/interview")
def interview(request: InterviewRequest):

    return process(request)