from fastapi import HTTPException
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
        if request.candidate is None:
            raise HTTPException(
                status_code=400,
                detail="Candidate information is required to start an interview."
            )

        candidate = None

        for c in candidates["candidates"]:
            if c["member"]["id"] == request.candidate.member.id:
                candidate = c
                break

        if candidate is None:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found."
            )

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
            "completed": False,
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

    session = sessions[request.sessionId]

    if session["completed"]:
        raise HTTPException(
            status_code=400,
            detail="Interview session is already completed."
        )

    current_question = session["current_question"]

    # ---------------------------------------------------------
    # EVALUATE ANSWER
    # ---------------------------------------------------------

    result = evaluate_answer(
        current_question,
        request.message
    )

    # The answer just submitted becomes part of the history.
    session["history"].append({
        "question": current_question,
        "answer": request.message,
        "score": result["score"],
        "feedback": result["feedback"],
        "curriculum_day": session["current_day"]
    })

    # Number of answers/questions actually completed
    questions_answered = len(session["history"])

    # ---------------------------------------------------------
    # CHECK WHETHER WE HAVE COMPLETED THE REQUIREMENTS
    # ---------------------------------------------------------
    #
    # The interview must:
    #   1. Have at least 8 answered questions
    #   2. Cover at least 4 curriculum days
    #
    # IMPORTANT:
    # We check this BEFORE generating another question.
    # Therefore, once Q8 is answered and 4 days are covered,
    # we finish immediately instead of generating Q9.
    #

    if (
        questions_answered >= MIN_QUESTIONS
        and len(session["covered_days"]) >= MIN_CURRICULUM_DAYS
    ):
        final_evaluation = generate_final_evaluation(
            session["history"]
        )

        session["completed"] = True

        return {
            "reply": "Interview completed.",
            "score": result["score"],
            "feedback": result["feedback"],
            "question_number": questions_answered,
            "curriculum_day": session["current_day"],
            "done": True,
            "final_evaluation": final_evaluation
        }

    # ---------------------------------------------------------
    # DETERMINE WHETHER TO CHANGE CURRICULUM DAY
    # ---------------------------------------------------------

    covered_days = session["covered_days"]
    curriculum = load_curriculum()

    # ---------------------------------------------------------
    # WEAK ANSWER
    # ---------------------------------------------------------
    #
    # Normally, a weak answer gets a follow-up on the same topic.
    #
    # BUT:
    # If we have not yet covered 4 curriculum days, staying on
    # the same day forever could make the interview impossible
    # to complete.
    #
    # Therefore, after a weak answer we only stay on the current
    # topic if doing so will not prevent us from reaching the
    # required curriculum-day coverage.
    #

    if result["score"] < 8:

        # We still need more curriculum days.
        # If we are already at/near the point where remaining
        # questions must be used to discover new days, move on.
        #
        # Example:
        # Q1-Q2 -> Day A
        # Q3-Q4 -> Day B
        # Q5-Q6 -> Day C
        # Q7     -> Day D
        #
        # This prevents "idk" from trapping the interview.
        remaining_required_days = (
            MIN_CURRICULUM_DAYS - len(covered_days)
        )

        remaining_questions = (
            MIN_QUESTIONS - questions_answered
        )

        if (
            remaining_required_days > 0
            and remaining_questions <= remaining_required_days
        ):
            # We MUST move to a new curriculum day.
            next_topic = choose_topic(
                session["candidate"],
                curriculum,
                excluded_days=covered_days
            )

            next_day = next_topic["day"]

            if next_day not in covered_days:
                covered_days.add(next_day)

                next_question = generate_question(
                    next_topic
                )

                session["current_topic"] = next_topic
                session["current_day"] = next_day
                session["current_question"] = next_question

            else:
                # Safety fallback if topic selector cannot provide
                # a new day.
                next_question = generate_question(
                    session["current_topic"],
                    session["history"],
                    result
                )

                session["current_question"] = next_question

        else:
            # Normal adaptive follow-up.
            next_question = generate_question(
                session["current_topic"],
                session["history"],
                result
            )

            session["current_question"] = next_question

    # ---------------------------------------------------------
    # STRONG ANSWER
    # ---------------------------------------------------------
    #
    # Strong answers naturally move the interview to a new day.
    #

    else:

        next_topic = choose_topic(
            session["candidate"],
            curriculum,
            excluded_days=covered_days
        )

        next_day = next_topic["day"]

        if next_day not in covered_days:

            covered_days.add(next_day)

            next_question = generate_question(
                next_topic
            )

            session["current_topic"] = next_topic
            session["current_day"] = next_day
            session["current_question"] = next_question

        else:

            # Safety fallback if no new day is available.
            next_question = generate_question(
                session["current_topic"],
                session["history"],
                result
            )

            session["current_question"] = next_question

    # ---------------------------------------------------------
    # UPDATE QUESTION NUMBER
    # ---------------------------------------------------------
    #
    # question_number represents the NEXT question that will
    # be displayed to the candidate.
    #

    session["question_number"] = questions_answered + 1

    return {
        "reply": session["current_question"],
        "score": result["score"],
        "feedback": result["feedback"],
        "question_number": session["question_number"],
        "curriculum_day": session["current_day"],
        "done": False
    }

