from fastapi import APIRouter
from models.request import InterviewRequest
from services.interview_service import process

router = APIRouter()


@router.post("/api/interview")
def interview(request: InterviewRequest):

    return process(request)