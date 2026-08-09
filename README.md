# 🤖 AI Interview Agent

An AI-powered technical interview platform designed to simulate realistic, personalized interviews for learners completing the 31-Day AI Cohort.

The AI Interview Agent conducts dynamic, multi-turn technical interviews based on curriculum topics and candidate learning profiles. Instead of presenting a fixed questionnaire, the system selects relevant topics, generates interview questions, evaluates candidate responses, and asks adaptive follow-up questions based on the quality of each answer.

The system maintains interview session history and uses it to keep the conversation coherent while tracking curriculum coverage. At the end of the interview, it generates a structured evaluation covering the candidate's technical performance, strengths, weaknesses, communication quality, and overall recommendation.

## ✨ Key Features

* 🎯 Personalized interview generation based on candidate learning progress
* 🤖 AI-generated technical interview questions
* 🔄 Adaptive follow-up questions based on candidate responses
* 🧠 Session-based conversation history and context
* 📚 Curriculum-aware topic selection
* 📈 Evaluation of candidate responses and technical understanding
* 📊 Structured final performance evaluation and feedback
* 💬 Communication-quality assessment
* 🔗 RESTful HTTP API for interview execution and frontend integration
* 🛠️ Modular backend architecture for future enhancements

## 🎯 Objectives

The primary objectives of this project are to:

* Simulate a realistic AI-assisted technical interview.
* Assess candidate knowledge across multiple AI engineering topics.
* Generate follow-up questions based on previous answers.
* Maintain context throughout an interview session.
* Track curriculum coverage during the interview.
* Provide structured feedback highlighting strengths and weaknesses.
* Provide an API that can be integrated with a frontend or learning platform.

## 🏗️ How It Works

1. **Candidate Identification**
   The system identifies the candidate from the provided candidate information.

2. **Curriculum-Aware Topic Selection**
   Available curriculum topics are determined from the candidate's learning profile.

3. **Question Generation**
   The LLM generates a technical interview question based on the selected curriculum topic.

4. **Answer Evaluation**
   The candidate's response is evaluated for its quality and understanding of the topic.

5. **Adaptive Interviewing**
   Strong answers can move the interview toward a new curriculum topic, while weaker answers can result in follow-up questions on the current topic.

6. **Interview Completion**
   The interview continues until the required number of questions and curriculum coverage requirements are satisfied.

7. **Final Evaluation**
   The system generates a structured final assessment containing an overall score, strengths, weaknesses, technical assessment, communication assessment, and recommendation.

## 🚀 Project Vision

The project demonstrates how Generative AI and LLMs can be used to create a more interactive approach to technical interview preparation.

Rather than relying on a static list of questions, the AI Interview Agent creates an interview that responds to the candidate's answers and learning context. The long-term vision is to expand this approach with richer candidate profiling, more sophisticated difficulty adaptation, broader evaluation criteria, and additional interview scenarios.

The current implementation focuses on establishing the core interview-agent workflow: curriculum-aware topic selection, AI-generated questions, response evaluation, adaptive follow-ups, session history, and structured final feedback.
