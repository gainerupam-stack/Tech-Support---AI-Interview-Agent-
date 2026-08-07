def evaluate_answer(question, answer):
    """
    Temporary evaluator.
    Later this will call an LLM.
    """

    if len(answer.strip()) > 40:
        return {
            "score": 8,
            "feedback": "Good answer."
        }

    return {
        "score": 3,
        "feedback": "Please explain in more detail."
    }