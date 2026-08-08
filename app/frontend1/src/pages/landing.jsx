function Landing({ onStart }) {
  return (
    <main>
      <h1>AI Interview Agent</h1>

      <p>
        Practice realistic interviews with an AI interviewer
        and receive feedback on your performance.
      </p>

      <button onClick={onStart}>
        Start Interview
      </button>
    </main>
  )
}

export default Landing