# app/services/interview_service.py
from app.services.data_loader import load_curriculum, load_candidates
from app.services.topic_selector import choose_topic
from app.services.question_generator import generate_question
from app.services.evaluator import evaluate_answer
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

        session = sessions[request.sessionId]
    
        # Save the candidate's answer
        session["history"].append({
            "question": session["current_question"],
            "answer": request.message
        })
    
        # Evaluate the current answer
        result = evaluate_answer(
            session["current_question"],
            request.message
        )
    
        # Generate the next question
        next_question = generate_question(
            session["current_topic"]
        )
    
        # Move to the next question
        session["question_number"] += 1
        session["current_question"] = next_question
    
        return {
            "reply":
            f"Score: {result['score']}/10\n"
            f"Feedback: {result['feedback']}\n\n"
            f"Question {session['question_number']}:\n\n"
            f"{next_question}",
            "done": False
        }