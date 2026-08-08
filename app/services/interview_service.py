from app.services.data_loader import load_curriculum, load_candidates
from app.services.topic_selector import choose_topic, get_available_topics
from app.services.question_generator import generate_question
from app.services.evaluator import evaluate_answer
from app.services.final_evaluator import generate_final_evaluation

sessions = {}

MIN_QUESTIONS = 8
MIN_CURRICULUM_DAYS = 4

def process(request):

# ---------------------------------------------------------
# FIRST REQUEST — START INTERVIEW
# ---------------------------------------------------------

    if request.sessionId not in sessions:
    
        curriculum = load_curriculum()
        candidates = load_candidates()
    
        # Find candidate
        candidate = None
    
        for c in candidates["candidates"]:
            if c["member"]["id"] == request.candidate["id"]:
                candidate = c
                break
    
        if candidate is None:
            return {
                "reply": "Candidate not found.",
                "done": True
            }
    
        # Get all curriculum topics available to this candidate
        available_topics = get_available_topics(
            candidate,
            curriculum
        )
    
        # Choose the first topic
        topic = choose_topic(
            candidate,
            curriculum,
            excluded_days=set()
        )
    
        question = generate_question(topic)
    
        curriculum_day = topic["day"]
    
        # Create session
        sessions[request.sessionId] = {
            "candidate": candidate,
            "history": [],
    
            "question_number": 1,
    
            "current_topic": topic,
            "current_question": question,
            "current_day": curriculum_day,
    
            "covered_days": {curriculum_day},
    
            "available_topics": available_topics
        }
    
        return {
            "reply": question,
            "question_number": 1,
            "curriculum_day": curriculum_day,
            "done": False
        }
    
    # ---------------------------------------------------------
    # LATER REQUESTS — PROCESS ANSWER
    # ---------------------------------------------------------
    
    else:
    
        session = sessions[request.sessionId]
    
        current_question = session["current_question"]
    
        # Evaluate answer
        result = evaluate_answer(
            current_question,
            request.message
        )
        session["question_number"] += 1
        # Save interaction
        session["history"].append({
            "question": current_question,
            "answer": request.message,
            "score": result["score"],
            "feedback": result["feedback"],
            "curriculum_day": session["current_day"]
        })
    
        # -----------------------------------------------------
        # DETERMINE WHETHER TO CHANGE CURRICULUM DAY
        # -----------------------------------------------------
    
        covered_days = session["covered_days"]
        
        # Weak or incomplete answer → follow-up
        if result["score"] < 8:
        
            next_question = generate_question(
                session["current_topic"],
                session["history"],
                result
            )
        
            session["current_question"] = next_question
        
        # Strong answer → move to a new curriculum day
        else:
        
            curriculum = load_curriculum()
        
            next_topic = choose_topic(
                session["candidate"],
                curriculum,
                excluded_days=covered_days
            )
        
            next_day = next_topic["day"]
        
            # New curriculum day available
            if next_day not in covered_days:
        
                covered_days.add(next_day)
        
                next_question = generate_question(
                    next_topic
                )
        
                session["current_topic"] = next_topic
                session["current_day"] = next_day
                session["current_question"] = next_question
        
            # All available days already covered
            else:
        
                next_question = generate_question(
                    session["current_topic"],
                    session["history"],
                    result
                )
        
                session["current_question"] = next_question
    
        # -----------------------------------------------------
        # CHECK MINIMUM QUESTION REQUIREMENT
        # -----------------------------------------------------
    
        if (len(session["history"]) >= MIN_QUESTIONS and len(session["covered_days"]) >= MIN_CURRICULUM_DAYS):
            final_evaluation = generate_final_evaluation(session["history"])
        
            return {
                "reply": "Interview completed.",
                "score": result["score"],
                "feedback": result["feedback"],
                "done": True,
                "final_evaluation": final_evaluation
            }
    
        return {
            "reply": session["current_question"],
            "score": result["score"],
            "feedback": result["feedback"],
            "question_number": session["question_number"],
            "curriculum_day": session["current_day"],
            "done": False
        }