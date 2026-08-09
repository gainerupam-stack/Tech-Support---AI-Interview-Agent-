# AI Usage Log — AI Interview Agent (BACKEND)

This document records the prompts used with AI assistance during the development of the AI Interview Agent backend. The prompts were used for planning, implementation, debugging, testing, and deployment of the backend system.
---

## 1. Initial Backend Architecture and Project Planning

### Prompt

> Design the backend architecture for an AI Interview Agent based on the provided hackathon requirements. The backend should handle candidate eligibility, curriculum-based topic selection, question generation, answer evaluation, interview state, and final evaluation. Suggest an appropriate FastAPI project structure and explain how the components should interact.

### Reason

Used to establish the initial backend architecture and determine how the interview system should be separated into services such as data loading, topic selection, question generation, evaluation, and final evaluation.

---

## 2. FastAPI Backend Structure

### Prompt

> Help me build the FastAPI backend for the AI Interview Agent. Create the necessary application structure and API flow so that the frontend can start an interview, submit answers, receive questions and feedback, and eventually receive the final evaluation.

### Reason

Used to implement the main FastAPI application and establish the API contract required for the interview flow.

---

## 3. Loading Curriculum and Candidate Data

### Prompt

> Create a backend data-loading service for the curriculum and candidate data. The service should load the provided data files and make the candidate and curriculum information available to the interview system.

### Reason

Used to create the data-loading layer so that interview logic could operate on the supplied candidate and curriculum information instead of hardcoded values.

---

## 4. Candidate Identification

### Prompt

> Implement candidate lookup for the interview API. The request contains candidate.member.id, while the candidate records returned by the data loader contain the candidate ID inside the member object. Make sure the correct candidate is found and return an appropriate error when the candidate does not exist.

### Reason

Used to correctly connect an incoming interview request to the corresponding candidate record and avoid candidate lookup failures.

---

## 5. Curriculum Topic Selection

### Prompt

> Build a topic-selection service for the AI Interview Agent. It should select appropriate curriculum topics for a candidate while allowing already-covered curriculum days to be excluded so that the interview can progressively cover different parts of the curriculum.

### Reason

Used to create adaptive curriculum progression and prevent the interview from repeatedly selecting the same curriculum day.

---

## 6. Question Generation

### Prompt

> Implement the question-generation service for the AI Interview Agent. Given a selected curriculum topic, generate an interview question appropriate to that topic. The system should also be able to generate follow-up questions using the previous question, interview history, and evaluation result.

### Reason

Used to implement the LLM-powered question generation component and support adaptive follow-up questions.

---

## 7. LLM Integration

### Prompt

> Integrate the LLM into the backend question-generation and evaluation services. Use the configured API credentials from the environment rather than hardcoding secrets. Structure the service so the rest of the application can call it without directly handling the API details.

### Reason

Used to connect the backend interview logic to the LLM while keeping API credentials outside the source code and separating LLM functionality from the API layer.

---

## 8. Answer Evaluation

### Prompt

> Build an answer-evaluation service for the AI Interview Agent. Given the current interview question and the candidate's answer, evaluate the answer and return a numerical score and useful feedback that can be used by the interview controller to decide whether a follow-up question or a new topic should be selected.

### Reason

Used to make the interview adaptive based on candidate performance.

---

## 9. Adaptive Interview Logic

### Prompt

> Implement the interview processing logic. A strong answer should generally move the candidate to a new curriculum day, while a weak or incomplete answer should normally produce a follow-up question on the current topic. Maintain the interview history and curriculum days covered during the session.

### Reason

Used to implement the core adaptive behavior of the interview agent.

---

## 10. Interview Session State

### Prompt

> Add session management to the interview backend. Each session should maintain the candidate, interview history, current topic, current question, current curriculum day, covered curriculum days, question number, and completion status. Use the session ID from the API request to identify the interview session.

### Reason

Used to allow multiple API requests to participate in the same interview while preserving the state of that interview.

---

## 11. Minimum Interview Requirements

### Prompt

> Modify the interview controller so that an interview cannot finish before at least 8 questions have been answered and at least 4 curriculum days have been covered. Once both requirements are satisfied, generate the final evaluation immediately rather than generating another question.

### Reason

Used to enforce the minimum interview requirements and prevent unnecessary additional questions after the required interview coverage had been achieved.

---

## 12. Preventing Weak Answers from Blocking Curriculum Coverage

### Prompt

> Fix the adaptive interview logic so that repeated weak answers cannot prevent the interview from reaching the required number of curriculum days. Weak answers should normally receive follow-up questions, but when the remaining number of questions makes it necessary to cover a new curriculum day, move to a new day instead.

### Reason

Used to prevent an edge case where repeated weak answers could trap the interview on one curriculum topic and make the minimum four-day requirement impossible to satisfy.

---

## 13. Correct Question Numbering

### Prompt

> Fix the interview question numbering. The question number returned by the API should accurately represent the question being presented, and when the candidate answers the eighth question and the minimum requirements are satisfied, the interview should complete instead of generating question nine.

### Reason

Used to correct the distinction between questions already answered and the next question to be displayed.

---

## 14. Final Evaluation

### Prompt

> Build the final evaluation service for the completed interview. Use the complete interview history to generate an overall assessment containing an overall score, strengths, weaknesses, technical assessment, communication assessment, and hiring recommendation.

### Reason

Used to generate a comprehensive evaluation after the interview rather than evaluating each answer independently only.

---

## 15. Communication Quality Assessment

### Prompt

> Include communication quality and grammar assessment in the final evaluation, but do not make grammar a major component of the overall technical score. The evaluation should distinguish communication quality from technical knowledge.

### Reason

Used to ensure the final evaluation considers communication ability without allowing grammar to disproportionately affect the candidate's technical assessment.

---

## 16. API Error Handling

### Prompt

> Add appropriate FastAPI HTTP errors for invalid interview requests, missing candidate information, unknown candidates, and attempts to submit answers to an already completed interview session.

### Reason

Used to make the backend API fail predictably and provide meaningful error responses to the client.

---

## 17. Backend API Testing

### Prompt

> Test the FastAPI interview endpoint using realistic request payloads. Verify that a session can be started with a valid candidate, answers can be submitted using the session ID, questions progress correctly, curriculum days are tracked, and the interview eventually returns done=true with the final evaluation.

### Reason

Used to verify the complete backend interview lifecycle rather than testing individual services in isolation.

---

## 18. Debugging the Interview Completion Flow

### Prompt

> The interview is reaching question 8 and returning "Interview completed." Verify that the backend is correctly enforcing the 8-question and 4-curriculum-day requirements and that the final evaluation is generated from the complete interview history.

### Reason

Used to validate the final interview state and ensure the completion response contained the expected final evaluation.

---

## 19. Uvicorn / Local Backend Execution

### Prompt

> Help me start the FastAPI backend locally using Uvicorn, including the correct command for the project structure and the virtual environment.

### Reason

Used to run and locally test the backend during development.

---

## 20. Virtual Environment / Dependency Debugging

### Prompt

> Uvicorn is not recognized when I run it from PowerShell, and the project's virtual environment cannot currently be activated because of the PowerShell execution policy. Help me run the backend using the virtual environment directly and install the required dependencies from requirements.txt.

### Reason

Used to resolve local development environment issues without changing the application code.

---

## 21. Backend Dependencies

### Prompt

> Check the backend requirements and make sure the dependencies required by the FastAPI application, Uvicorn server, Pydantic models, environment configuration, and Groq LLM integration are included in requirements.txt.

### Reason

Used to make sure the backend could be installed and run consistently in deployment environments.

---

## 22. Environment Variables and Secrets

### Prompt

> Make sure the backend uses environment variables for API credentials and configuration rather than storing secrets directly in the repository. Ensure the application can load the required environment variables during local development and deployment.

### Reason

Used to keep credentials out of source control and make the application compatible with deployment platforms.

---

## 23. Render Deployment

### Prompt

> Help me deploy the FastAPI backend to Render. Configure the application so Render can install the requirements, start the FastAPI/Uvicorn server, and expose the API publicly. Make sure the deployment uses the correct host and port configuration provided by Render.

### Reason

Used to make the backend publicly accessible so the interview application could be used outside the developer's local machine.

---

## 24. Deployment Verification

### Prompt

> The FastAPI backend is running locally and has also been deployed to Render. Help me verify that the public Render API is serving the latest backend code and that the interview endpoint works after deployment.

### Reason

Used to verify that the deployed backend matched the locally tested implementation.

---

## 25. Backend / Frontend API Contract

### Prompt

> Review the backend API response and request structure and make sure it provides the fields required by the interview client, including reply, score, feedback, question_number, curriculum_day, done, and final_evaluation when the interview is complete.

### Reason

Used to establish a stable API contract between the backend interview system and the client consuming it.

---

## 26. Final Backend Interview Processing Logic

### Prompt

> Review and fix the complete interview processing function. It must:
>
> * start a new interview when the session ID is new;
> * validate and locate the candidate;
> * select the initial curriculum topic;
> * generate the first question;
> * preserve interview state;
> * evaluate submitted answers;
> * record interview history;
> * generate follow-up questions for weak answers;
> * move to new curriculum days for strong answers;
> * ensure at least 8 questions are answered;
> * ensure at least 4 curriculum days are covered;
> * generate the final evaluation when the requirements are met;
> * return a consistent API response.

### Reason

Used as the final integration pass over the backend interview controller, combining the previously implemented components into one complete interview workflow.

---

# Summary of AI Assistance

AI assistance was used throughout backend development for:

1. Backend architecture and planning
2. FastAPI implementation
3. Data loading
4. Candidate lookup
5. Curriculum/topic selection
6. LLM-based question generation
7. Adaptive follow-up questions
8. Answer evaluation
9. Interview session management
10. Curriculum-day progression
11. Interview completion requirements
12. Final candidate evaluation
13. Communication-quality assessment
14. Error handling
15. Local testing and debugging
16. Dependency and environment setup
17. Uvicorn execution
18. Render deployment and verification
19. API contract validation
20. Final integration and debugging

The AI was used as a development and debugging assistant. The resulting backend was tested and iteratively modified to satisfy the application's interview requirements and deployment constraints.

---

## Excluded Work

The following work is intentionally not represented in this log because it belonged to the frontend/frontend-testing work rather than the backend interview-agent implementation:

* React frontend development
* Frontend HTML/CSS/JavaScript implementation
* Frontend-testing branch development
* Frontend UI design
* Frontend-only debugging
* Client-side state management
* Frontend Live Server issues
* Frontend-specific API integration changes
