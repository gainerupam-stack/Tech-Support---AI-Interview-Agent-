const API_URL = "https://tech-support-ai-interview-agent.onrender.com"

export async function getCandidates() {
  const response = await fetch(`${API_URL}/api/candidates`)

  if (!response.ok) {
    throw new Error("Failed to fetch candidates")
  }

  return response.json()
}

export async function startInterview(sessionId, candidateId) {
  const response = await fetch(`${API_URL}/api/interview`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      sessionId,
      candidate: {
        id: candidateId,
      },
    }),
  })

  if (!response.ok) {
    throw new Error("Failed to start interview")
  }

  return response.json()
}

export async function sendAnswer(sessionId, message) {
  const response = await fetch(`${API_URL}/api/interview`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      sessionId,
      message,
    }),
  })

  if (!response.ok) {
    throw new Error("Failed to submit answer")
  }

  return response.json()
}