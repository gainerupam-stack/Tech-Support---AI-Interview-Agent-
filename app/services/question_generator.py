from app.services.llm_service import ask_llm

def generate_question(topic, history=None, latest_evaluation=None):

    history = history or []

    prompt = f"""
    
    You are an expert technical interviewer.
    
    Generate the next interview question for the candidate.
    
    CURRENT TOPIC:
    {topic}
    
    PREVIOUS INTERVIEW HISTORY:
    {history}
    
    LATEST EVALUATION:
    {latest_evaluation}
    
    Rules:
    
    Ask exactly ONE question.
    Do not repeat a previous question.
    Use the previous answers and evaluation to decide what to ask next.
    If the candidate performed poorly, ask a question that probes the same concept
    but is simpler or helps identify what they misunderstood.
    If the candidate performed well, increase the difficulty slightly.
    If the candidate has demonstrated strong understanding of the current concept,
    explore a related concept within the same topic.
    The question should test understanding, not memorization.
    Do not provide the answer.
    
    Return ONLY the question. Do not include labels such as "Question:".
    """
    
    return ask_llm(prompt).strip()