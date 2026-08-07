# app/services/interview_service.py
from services.data_loader import load_curriculum, load_candidates
from services.topic_selector import choose_topic
sessions = {}


def process(request):

    # First request of interview
    if request.sessionId not in sessions:

        curriculum = load_curriculum()
        candidates = load_candidates()
        # Find the candidate in candidates.json
        candidate = None

        for c in candidates["candidates"]:
              if c["member"]["id"] == request.candidate["id"]:
                   candidate = c
                   break

        # Choose an interview topic
        if candidate is None:
            return {"reply": "Candidate not found.","done": True}
        topic = choose_topic(candidate, curriculum)

        sessions[request.sessionId] = {
            "candidate": request.candidate,
            "history": [],
            "question_number": 1
        }

        return {
             "reply": f"Welcome. Let's begin with {topic['title']}.", "done": False
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