def generate_question(topic):

    questions = {
        "Embeddings Explained":
            "What are embeddings, and why are they useful in AI applications?",

        "Vector Databases Overview":
            "What problem does a vector database solve?",

        "Retrieval & Matching Engine":
            "How does semantic search differ from keyword search?",

        "Prompt Engineering Fundamentals":
            "What is the difference between zero-shot and few-shot prompting?",

        "Chatbot Backend & API Integration":
            "How would you design a FastAPI endpoint for a chatbot?",

        "Multi-Agent Orchestration":
            "Why would you use multiple AI agents instead of one?",

        "Model Context Protocol (MCP)":
            "Can you explain what MCP is and why it exists?",

        "Docker & Kubernetes Deployment":
            "Why is Docker useful when deploying AI applications?"
    }

    return questions.get(
        topic["title"],
        "Tell me about one project you are proud of."
    )