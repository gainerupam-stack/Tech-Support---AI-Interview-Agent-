import { useState } from "react"
import Landing from "./pages/Landing"
import Setup from "./pages/Setup"
import Interview from "./pages/Interview"

function App() {
  const [page, setPage] = useState("landing")
  const [candidate, setCandidate] = useState(null)

  function handleSetup(candidateData) {
    setCandidate(candidateData)
    setPage("interview")
  }

  return (
    <>
      {page === "landing" && (
        <Landing onStart={() => setPage("setup")} />
      )}

      {page === "setup" && (
        <Setup onStart={handleSetup} />
      )}

      {page === "interview" && (
        <Interview candidate={candidate} />
      )}
    </>
  )
}

export default App