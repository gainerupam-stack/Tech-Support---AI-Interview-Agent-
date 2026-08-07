# app/services/interview_service.py
from services.data_loader import load_curriculum, load_candidates
sessions = {}


def process(request):

    # First request of interview
    if request.sessionId not in sessions:
        
        curriculum = load_curriculum()
        candidates = load_candidates()
        print(curriculum)
        print(candidates)

        sessions[request.sessionId] = {
            "candidate": request.candidate,
            "history": [],
            "question_number": 1
        }

        return {
            "reply": "Welcome. Let's begin your interview.",
            "done": False
        }

    # Later requests
    else:

        sessions[request.sessionId]["history"].append(
            request.message
        )

        sessions[request.sessionId]["question_number"] += 1

        return {
            "reply": f"Question {sessions[request.sessionId]['question_number']}",
            "done": False
        }