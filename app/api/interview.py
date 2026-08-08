from fastapi import APIRouter
from app.models.request import InterviewRequest
from app.models.response import InterviewResponse
from app.services.interview_service import process

router = APIRouter()


@router.post("/api/interview", response_model=InterviewResponse)
def interview(request: InterviewRequest):

    return process(request)