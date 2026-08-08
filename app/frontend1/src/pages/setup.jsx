import { useEffect, useState } from "react"
import { getCandidates } from "../api"

function Setup({ onStart }) {
  const [candidates, setCandidates] = useState([])
  const [selectedId, setSelectedId] = useState("")
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    async function loadCandidates() {
      try {
        const data = await getCandidates()
        setCandidates(data.candidates)
      } catch (error) {
        setError("Could not load candidates.")
        console.error(error)
      } finally {
        setLoading(false)
      }
    }

    loadCandidates()
  }, [])

  function handleSubmit(event) {
    event.preventDefault()

    if (!selectedId) {
      return
    }

    onStart({
      id: selectedId,
    })
  }

  if (loading) {
    return <p>Loading candidates...</p>
  }

  if (error) {
    return <p>{error}</p>
  }

  return (
    <main>
      <h1>Interview Setup</h1>

      <p>Select the candidate you want to interview.</p>

      <form onSubmit={handleSubmit}>
        <label>
          Candidate
        </label>

        <select
          value={selectedId}
          onChange={(event) => setSelectedId(event.target.value)}
          required
        >
          <option value="">Select a candidate</option>

          {candidates.map((candidate) => (
            <option key={candidate.id} value={candidate.id}>
              {candidate.name} — {candidate.jobRole}
            </option>
          ))}
        </select>

        <button type="submit">
          Begin Interview
        </button>
      </form>
    </main>
  )
}

export default Setup