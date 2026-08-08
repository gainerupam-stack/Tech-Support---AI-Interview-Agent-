from app.services.llm_service import ask_llm

def generate_question(topic, history=None, evaluation=None):

    history = history or []
    
    # ---------------------------------------------------------
    # FOLLOW-UP QUESTION
    # ---------------------------------------------------------
    
    if evaluation is not None and history:
    
        previous = history[-1]
    
        prompt = f"""
    
    You are an expert technical interviewer conducting an adaptive interview.
    
    The candidate is being interviewed on this curriculum topic:
    
    TOPIC:
    {topic}
    
    PREVIOUS QUESTION:
    {previous["question"]}
    
    CANDIDATE'S ANSWER:
    {previous["answer"]}
    
    EVALUATION:
    Score: {evaluation["score"]}/10
    Feedback: {evaluation["feedback"]}
    
    Generate ONE follow-up technical interview question.
    
    The follow-up should investigate something the candidate:
    
    explained incorrectly,
    explained incompletely,
    or could demonstrate more deeply.
    
    Do not simply repeat the previous question.
    
    If the candidate's answer was strong, ask a deeper technical question
    that tests whether they actually understand the concept.
    
    Return ONLY the question.
    """
    
        return ask_llm(prompt).strip()
    
    # ---------------------------------------------------------
    # NEW CURRICULUM TOPIC
    # ---------------------------------------------------------
    
    prompt = f"""
    
    You are an expert technical interviewer.
    
    Create ONE technical interview question based on this curriculum topic:
    
    {topic}
    
    The question should:
    
    test actual technical understanding,
    be appropriate for a professional software engineer,
    require reasoning rather than memorization,
    be answerable verbally,
    not contain multiple unrelated questions.
    
    Return ONLY the interview question.
    """
    
    return ask_llm(prompt).strip()