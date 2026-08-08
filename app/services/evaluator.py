from app.services.llm_service import ask_llm

def evaluate_answer(question, answer):

    prompt = f"""

    You are an expert technical interviewer.

    Evaluate the candidate's answer to the interview question below.

    QUESTION:
    {question}

    CANDIDATE ANSWER:
    {answer}

    Evaluate the answer on:
    
    Correctness
    Relevance
    Technical understanding
    Clarity
    
    Give a score from 0 to 10.
    
    Return your response in exactly this format:
    
    SCORE: <number>
    FEEDBACK: <short explanation>
    
    Do not be overly harsh.
    Do not give a high score simply because the answer is long.
    Focus on whether the candidate actually understands the concept.
    """

    text = ask_llm(prompt)

    score = 0
    feedback = text

    for line in text.splitlines():

        if line.startswith("SCORE:"):
            try:
                score = float(line.replace("SCORE:", "").strip())
            except ValueError:
                score = 0

        elif line.startswith("FEEDBACK:"):
            feedback = line.replace("FEEDBACK:", "").strip()

    return {
             "score": score,
             "feedback": feedback
}