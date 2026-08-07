from services.llm_service import ask_llm

def generate_question(topic):

    prompt = f"""
You are an AI technical interviewer.

Generate ONE interview question.

Topic:
Title: {topic["title"]}
Type: {topic["type"]}

Learning objectives:
{chr(10).join("- " + obj for obj in topic["objectives"])}

Return only the interview question.
"""

    return ask_llm(prompt)