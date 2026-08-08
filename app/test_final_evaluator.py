from app.services.final_evaluator import generate_final_evaluation


history = [
    {
        "question": "What is polymorphism in object-oriented programming?",
        "answer": "Polymorphism means the same interface can be used for different implementations.",
        "score": 8,
        "feedback": "Good understanding of the concept.",
        "curriculum_day": 3
    },
    {
        "question": "What is a virtual environment in Python?",
        "answer": "It isolates dependencies for a project so different projects can use different package versions.",
        "score": 9,
        "feedback": "Correct and clearly explained.",
        "curriculum_day": 1
    },
    {
        "question": "What are embeddings used for?",
        "answer": "They convert data into vectors that capture semantic meaning.",
        "score": 7,
        "feedback": "Correct but could use more detail.",
        "curriculum_day": 7
    }
]


result = generate_final_evaluation(history)

print("\n===== FINAL INTERVIEW EVALUATION =====\n")
print(result)