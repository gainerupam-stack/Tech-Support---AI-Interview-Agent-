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

        # Get the question that the candidate is answering 
        current_question = session["current_question"] 

        # Evaluate the candidate's answer 
        result = evaluate_answer( current_question, request.message ) 
        # Save the complete interaction to interview history 
        session["history"].append({ "question": current_question, 
                                   "answer": request.message, 
                                   "score": result["score"], 
                                   "feedback": result["feedback"] }) 
        
        # Generate the next question using the interview history 
        next_question = generate_question(session["current_topic"], 
                                          session["history"], result ) 
        # Move to the next question 
        session["question_number"] += 1 
        session["current_question"] = next_question 
        return { "reply": 
                f"Score: {result['score']}/10\n" 
                f"Feedback: {result['feedback']}\n\n" 
                f"Question {session['question_number']}:\n\n" 
                f"{next_question}", "done": False }