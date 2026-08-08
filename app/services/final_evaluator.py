from app.services.llm_service import client


def generate_final_evaluation(history):
    
    # Build a readable transcript of the interview
    transcript = ""

    for i, item in enumerate(history, start=1):
        transcript += f"""
QUESTION {i}:
{item["question"]}

CANDIDATE ANSWER:
{item["answer"]}

SCORE:
{item["score"]}/10

FEEDBACK:
{item["feedback"]}

CURRICULUM DAY:
{item["curriculum_day"]}

--------------------------------
"""

    prompt = f"""
You are a senior technical interviewer.

You have just completed a technical interview.

Analyze the complete interview transcript below and produce a
structured final evaluation of the candidate.

INTERVIEW TRANSCRIPT:

{transcript}

Evaluate the candidate based primarily on:

1. Technical knowledge
2. Problem solving ability
3. Understanding of concepts
4. Ability to explain technical ideas
5. Consistency across the interview

Also assess:

6. Communication clarity and language quality, including grammar

Communication quality should be treated as a supporting factor, not a major component of the overall score. Do not penalize a candidate heavily for minor grammatical mistakes if their technical understanding and reasoning are strong.

Identify:

7. Strengths
8. Weaknesses

Return your response in EXACTLY this format:

OVERALL_SCORE: <number from 0 to 10>

STRENGTHS:
- <strength 1>
- <strength 2>
- <strength 3>

WEAKNESSES:
- <weakness 1>
- <weakness 2>
- <weakness 3>

TECHNICAL_ASSESSMENT:
<short paragraph>

COMMUNICATION_ASSESSMENT:
<short paragraph about clarity, grammar, and communication quality>

RECOMMENDATION:
<short hiring/interview recommendation>

Do not invent information that is not supported by the interview.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a senior technical interviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content