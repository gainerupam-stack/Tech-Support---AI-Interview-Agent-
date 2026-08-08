from services.evaluator import evaluate_answer


question = "What is polymorphism in object-oriented programming?"

answer = """
Polymorphism means that the same interface can be used
for different implementations. Different classes can
implement the same method in different ways.
"""


result = evaluate_answer(question, answer)

print(result)