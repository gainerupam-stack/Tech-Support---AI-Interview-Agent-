from fastapi import APIRouter
from app.models.request import InterviewRequest
from app.services.interview_service import process
from app.services.data_loader import load_candidates

router = APIRouter()


@router.get("/api/candidates")
def get_candidates():

    candidates = load_candidates()

    return {
        "candidates": [
            candidate["member"]
            for candidate in candidates["candidates"]
        ]
    }


@router.post("/api/interview")
def interview(request: InterviewRequest):

    return process(request)