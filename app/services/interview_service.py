from app.services.data_loader import load_curriculum, load_candidates
from app.services.topic_selector import choose_topic, get_available_topics
from app.services.question_generator import generate_question
from app.services.evaluator import evaluate_answer

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
            "reply": (
                "Welcome!\n\n"
                "First Question:\n\n"
                f"{question}"
            ),
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
    
        # Save interaction
        session["history"].append({
            "question": current_question,
            "answer": request.message,
            "score": result["score"],
            "feedback": result["feedback"],
            "curriculum_day": session["current_day"]
        })
    
        questions_asked = session["question_number"]
    
        # -----------------------------------------------------
        # DETERMINE WHETHER TO CHANGE CURRICULUM DAY
        # -----------------------------------------------------
    
        covered_days = session["covered_days"]
    
        # If we have fewer than 4 curriculum days covered,
        # prioritize moving to a new curriculum day.
        if len(covered_days) < MIN_CURRICULUM_DAYS:
    
            next_topic = choose_topic(
                session["candidate"],
                load_curriculum(),
                excluded_days=covered_days
            )
    
            next_day = next_topic["day"]
    
            # If a new day was found, switch to it
            if next_day not in covered_days:
    
                covered_days.add(next_day)
    
                next_question = generate_question(
                    next_topic,
                    session["history"],
                    result
                )
    
                session["current_topic"] = next_topic
                session["current_day"] = next_day
                session["current_question"] = next_question
    
            else:
    
                # Fallback: adaptive follow-up
                next_question = generate_question(
                    session["current_topic"],
                    session["history"],
                    result
                )
    
                session["current_question"] = next_question
    
        else:
    
            # Once 4 curriculum days are covered,
            # focus on adaptive follow-up questions.
            next_question = generate_question(
                session["current_topic"],
                session["history"],
                result
            )
    
            session["current_question"] = next_question
    
        # Move to next question
        session["question_number"] += 1
    
        # -----------------------------------------------------
        # CHECK MINIMUM QUESTION REQUIREMENT
        # -----------------------------------------------------
    
        if (
            session["question_number"] > MIN_QUESTIONS
            and len(session["covered_days"]) >= MIN_CURRICULUM_DAYS
        ):
            return {
                "reply": (
                    f"Score: {result['score']}/10\n"
                    f"Feedback: {result['feedback']}\n\n"
                    "Interview requirements completed."
                ),
                "done": True
            }
    
        return {
            "reply": (
                f"Score: {result['score']}/10\n"
                f"Feedback: {result['feedback']}\n\n"
                f"Question {session['question_number']}:\n\n"
                f"{session['current_question']}"
            ),
            "done": False
        }