# app/services/interview_service.py
from services.data_loader import load_curriculum, load_candidates
from services.topic_selector import choose_topic
from services.question_generator import generate_question
from services.evaluator import evaluate_answer
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
        question = generate_question(topic)

        sessions[request.sessionId] = {
                "candidate": request.candidate,
                "history": [],
                "question_number": 1,
                "current_topic": topic,
                "current_question": question
                }

        return {
                "reply": f"Welcome!\n\nFirst Question:\n\n{question}","done": False
        }
    # Later requests
    else:

        sessions[request.sessionId]["history"].append(
            request.message
        )

        sessions[request.sessionId]["question_number"] += 1
        question = sessions[request.sessionId]["current_question"]
        result = evaluate_answer(question,request.message)
        return {
        "reply":
        f"Score: {result['score']}/10\n"
        f"Feedback: {result['feedback']}\n\n"
        f"Question {sessions[request.sessionId]['question_number']}",
         "done": False
                }