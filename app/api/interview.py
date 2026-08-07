from fastapi import APIRouter

router = APIRouter()


@router.post("/api/interview")
def interview(request: dict):

    return {
        "reply": "Welcome. Let's begin your interview.",
        "done": False
    }