import { useEffect, useState } from "react"
import { startInterview, sendAnswer } from "../api"

function Interview({ candidate }) {
  const [sessionId, setSessionId] = useState("")
  const [question, setQuestion] = useState("")
  const [answer, setAnswer] = useState("")
  const [feedback, setFeedback] = useState("")
  const [loading, setLoading] = useState(true)
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState("")

  useEffect(() => {
    async function beginInterview() {
      try {
        const newSessionId = crypto.randomUUID()

        setSessionId(newSessionId)

        const data = await startInterview(
          newSessionId,
          candidate.id
        )

        setQuestion(data.reply)
      } catch (error) {
        console.error(error)
        setError("Could not start the interview.")
      } finally {
        setLoading(false)
      }
    }

    beginInterview()
  }, [candidate])

  async function handleSubmit(event) {
    event.preventDefault()

    if (!answer.trim()) {
      return
    }

    setSubmitting(true)
    setFeedback("")
    setError("")

    try {
      const data = await sendAnswer(
        sessionId,
        answer
      )

      setFeedback(data.feedback || "")
      setQuestion(data.reply || "")
      setAnswer("")
    } catch (error) {
      console.error(error)
      setError("Could not submit your answer.")
    } finally {
      setSubmitting(false)
    }
  }

  if (loading) {
    return <p>Starting interview...</p>
  }

  if (error && !question) {
    return <p>{error}</p>
  }

  return (
    <main>
      <h1>AI Interview</h1>

      <p>{question}</p>

      {feedback && (
        <p>
          Feedback: {feedback}
        </p>
      )}

      {error && (
        <p>{error}</p>
      )}

      <form onSubmit={handleSubmit}>
        <textarea
          value={answer}
          onChange={(event) => setAnswer(event.target.value)}
          placeholder="Type your answer..."
          rows="6"
          disabled={submitting}
        />

        <br />

        <button
          type="submit"
          disabled={submitting}
        >
          {submitting ? "Evaluating..." : "Submit Answer"}
        </button>
      </form>
    </main>
  )
}

export default Interview