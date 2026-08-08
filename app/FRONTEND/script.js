const API_URL = "http://127.0.0.1:8000/api/interview";

const candidates = [
  {id:"CAND-001",name:"Sarah Johnson",jobRole:"Senior Data Engineer",yearsExperience:9,education:"MS Computer Science",signals:{commitDays:28,missionsCompleted:30,missionsFirstTry:20},missions:[7,8,10,12,16,22,23,28,29,31],skipped:[29]},
  {id:"CAND-002",name:"Alex Turner",jobRole:"Backend Software Engineer",yearsExperience:5,education:"B.Tech Computer Science",signals:{commitDays:22,missionsCompleted:29,missionsFirstTry:10},missions:[7,8,10,12,13,16,18,22,28,31],skipped:[]},
  {id:"CAND-003",name:"Emily Chen",jobRole:"AI Engineer",yearsExperience:6,education:"MS Artificial Intelligence",signals:{commitDays:31,missionsCompleted:31,missionsFirstTry:30},missions:[7,8,10,11,12,13,21,22,23,31],skipped:[]},
  {id:"CAND-004",name:"David Miller",jobRole:"Business Analyst",yearsExperience:8,education:"MBA",signals:{commitDays:18,missionsCompleted:28,missionsFirstTry:6},missions:[7,8,10,12,16,20,22,23,31],skipped:[28]},
  {id:"CAND-005",name:"Michael Brown",jobRole:"DevOps Engineer",yearsExperience:10,education:"B.Tech Information Technology",signals:{commitDays:30,missionsCompleted:31,missionsFirstTry:22},missions:[7,8,10,12,18,22,23,28,29,31],skipped:[]},
  {id:"CAND-006",name:"Wendy Foster",jobRole:"Marketing Manager",yearsExperience:12,education:"BA Marketing",signals:{commitDays:19,missionsCompleted:24,missionsFirstTry:2},missions:[1,7,8,12,16,17,22,31],skipped:[27,28]},
  {id:"CAND-007",name:"Ethan Brooks",jobRole:"Computer Science Intern",yearsExperience:0,education:"BS Computer Science (in progress)",signals:{commitDays:26,missionsCompleted:27,missionsFirstTry:22},missions:[1,3,7,8,12,16,22,31],skipped:[27,28]},
  {id:"CAND-008",name:"Harold Whitfield",jobRole:"Distinguished Engineer",yearsExperience:28,education:"BS Computer Science",signals:{commitDays:25,missionsCompleted:27,missionsFirstTry:15},missions:[1,4,5,21,22,23,27,28,31],skipped:[14,15]},
  {id:"CAND-009",name:"Zara Ahmadi",jobRole:"AI Engineer",yearsExperience:1,education:"BS Computer Science",signals:{commitDays:31,missionsCompleted:31,missionsFirstTry:29},missions:[7,8,10,12,13,21,22,23,27,31],skipped:[]},
  {id:"CAND-010",name:"Gerald Combs",jobRole:"IT Support Specialist",yearsExperience:20,education:"AAS Information Technology",signals:{commitDays:22,missionsCompleted:23,missionsFirstTry:1},missions:[1,7,12,16,31],skipped:[27,28],failed:[8,10,22]},
  {id:"CAND-011",name:"Mia Alvarez",jobRole:"UX Researcher",yearsExperience:6,education:"MA Human-Computer Interaction",signals:{commitDays:9,missionsCompleted:14,missionsFirstTry:5},missions:[1,2,3,4,31],skipped:[7,8,12,16,22]},
  {id:"CAND-012",name:"Chen Wei",jobRole:"Mobile App Developer",yearsExperience:7,education:"BS Computer Engineering",signals:{commitDays:27,missionsCompleted:30,missionsFirstTry:14},missions:[7,8,9,10,16,18,22,28,30,31],skipped:[]},
  {id:"CAND-013",name:"Ravi Patel",jobRole:"Software Engineer",yearsExperience:15,education:"MS Computer Science",signals:{commitDays:27,missionsCompleted:30,missionsFirstTry:13},missions:[1,4,7,8,12,16,22,27,28,31],skipped:[]},
  {id:"CAND-014",name:"Bethany Cole",jobRole:"HR Manager",yearsExperience:10,education:"BA Human Resources",signals:{commitDays:17,missionsCompleted:20,missionsFirstTry:1},missions:[1,7,12,16,20,31],skipped:[8,22,27,28]},
  {id:"CAND-015",name:"Noah Kim",jobRole:"Principal Architect",yearsExperience:20,education:"MS Computer Science",signals:{commitDays:29,missionsCompleted:29,missionsFirstTry:27},missions:[1,7,8,21,22,23,27,31],skipped:[14,15]},
  {id:"CAND-016",name:"Isabella Rossi",jobRole:"Software Engineer",yearsExperience:5,education:"BS Computer Science",signals:{commitDays:19,missionsCompleted:21,missionsFirstTry:2},missions:[1,8,16,31],skipped:[27,28],failed:[7,12,22]},
  {id:"CAND-017",name:"Tyler Brooks",jobRole:"Junior Developer",yearsExperience:0,education:"GED + Coding Bootcamp Certificate",signals:{commitDays:30,missionsCompleted:31,missionsFirstTry:1},missions:[1,3,7,8,10,12,16,22,28,31],skipped:[]},
  {id:"CAND-018",name:"Diane Foster",jobRole:"AI Engineer",yearsExperience:4,education:"MS Computer Science",signals:{commitDays:31,missionsCompleted:31,missionsFirstTry:31},missions:[7,8,10,12,13,22,23,27,28,31],skipped:[]},
  {id:"CAND-019",name:"Frank DeLuca",jobRole:"Legacy Systems Engineer",yearsExperience:25,education:"BS Computer Science",signals:{commitDays:26,missionsCompleted:29,missionsFirstTry:11},missions:[1,4,7,8,16,17,19,22,28,31],skipped:[]},
  {id:"CAND-020",name:"Priyanka Sharma",jobRole:"Software Engineer",yearsExperience:5,education:"BS Computer Science",signals:{commitDays:24,missionsCompleted:27,missionsFirstTry:19},missions:[1,3,12,16,22,27,31],skipped:[4,8],failed:[7]}
];

const dayTitles = {
  1:"Environment & Tooling",3:"First AI Project",4:"Structured Data",5:"Unstructured Data",7:"Embeddings",
  8:"Vector Databases",9:"Vector DB Build",10:"Retrieval Engine",11:"RAG & LLM APIs",12:"Prompt Engineering",
  13:"Function Calling",14:"Fine-Tuning Concepts",15:"LoRA & QLoRA",16:"Chatbot Backend",17:"Chatbot Frontend",
  18:"Streaming",19:"Rich Outputs",20:"Conversation Memory",21:"LangChain Agents",22:"Multi-Agent",
  23:"MCP",24:"Agentic Integration",25:"Evaluation",26:"Performance & Cost",27:"Security & Guardrails",
  28:"Docker & Kubernetes",29:"Observability",30:"Production Testing",31:"Capstone"
};

let state = {
  sessionId: null,
  active: false,
  questionCount: 0,
  coveredDays: new Set(),
  selectedCandidate: candidates[0]
};

const $ = id => document.getElementById(id);

function renderCandidateOptions() {
  $("candidateSelect").innerHTML = candidates.map(c =>
    `<option value="${c.id}">${c.name} · ${c.jobRole}</option>`
  ).join("");
}

function selectedCandidate() {
  return candidates.find(c => c.id === $("candidateSelect").value) || candidates[0];
}

function renderCandidate() {
  state.selectedCandidate = selectedCandidate();
  const c = state.selectedCandidate;
  $("candidateMeta").innerHTML =
    `<strong>${c.jobRole}</strong><br>${c.education}<br>${c.yearsExperience} years experience`;
  $("snapshot").innerHTML = `
    <div class="stat"><div class="stat-label">Completed missions</div><div class="stat-value">${c.signals.missionsCompleted}/31</div></div>
    <div class="stat"><div class="stat-label">First-try passes</div><div class="stat-value">${c.signals.missionsFirstTry}</div></div>
    <div class="stat"><div class="stat-label">Active / commit days</div><div class="stat-value">${c.signals.commitDays}/31</div></div>
  `;

  const focus = [];
  if (c.skipped?.length) focus.push(`Probe skipped areas: ${c.skipped.map(d => `Day ${d}`).join(", ")}`);
  if (c.failed?.length) focus.push(`Probe repeated challenge areas: ${c.failed.map(d => `Day ${d}`).join(", ")}`);
  focus.push(`Use ${c.jobRole} experience to test architecture trade-offs.`);
  focus.push("Follow strong answers with deeper why/how/production questions.");
  $("focusList").innerHTML = focus.map(x => `<div class="focus-item">${x}</div>`).join("");

  $("coverageList").innerHTML = c.missions.map(d =>
    `<span class="coverage-tag ${c.skipped?.includes(d) ? "" : "active"}">D${d}</span>`
  ).join("");
}

function resetUI() {
  state.sessionId = crypto.randomUUID();
  state.active = false;
  state.questionCount = 0;
  state.coveredDays = new Set();
  $("chat").innerHTML = `
    <div class="welcome-state">
      <div class="welcome-icon">✦</div>
      <h2>AI Interview Agent</h2>
      <p>Select a candidate and start a realistic, adaptive technical interview.</p>
      <div class="feature-row"><span>↳ Follow-ups</span><span>◈ Context-aware</span><span>✓ Structured feedback</span></div>
      <button id="startBtn" class="primary-btn">Start interview</button>
    </div>`;
  $("startBtn").onclick = startInterview;
  $("messageInput").disabled = true;
  $("sendBtn").disabled = true;
  $("sessionLabel").textContent = "No active session";
  $("feedbackPanel").classList.add("hidden");
  updateProgress();
}

function updateProgress() {
  $("progressText").textContent = `${state.questionCount} / 8+`;
  $("progressBar").style.width = `${Math.min(100, state.questionCount / 8 * 100)}%`;
}

function addMessage(role, text) {
  const wrap = document.createElement("div");
  wrap.className = `message-row ${role}`;
  const avatar = role === "user" ? "You" : "AI";
  wrap.innerHTML = `
    <div class="avatar">${avatar}</div>
    <div>
      <div class="bubble">${escapeHTML(text).replace(/\n/g, "<br>")}</div>
      <div class="msg-meta">${role === "user" ? "Candidate" : "Interviewer"} · just now</div>
    </div>`;
  $("chat").appendChild(wrap);
  $("chat").scrollTop = $("chat").scrollHeight;
}

function addTyping() {
  const el = document.createElement("div");
  el.id = "typing";
  el.className = "message-row";
  el.innerHTML = `<div class="avatar">AI</div><div class="bubble"><div class="typing"><i></i><i></i><i></i></div></div>`;
  $("chat").appendChild(el);
  $("chat").scrollTop = $("chat").scrollHeight;
}

function removeTyping() { $("typing")?.remove(); }

function addTurnFeedback(score, feedback) {
  if (score === undefined && !feedback) return;
  if (score === null && !feedback) return;
  const wrap = document.createElement("div");
  wrap.className = "turn-feedback";
  const scoreHTML = (score === null || score === undefined)
    ? ""
    : `<span class="turn-feedback-score">${escapeHTML(String(score))}/10</span>`;
  const feedbackHTML = feedback ? `<span>${escapeHTML(feedback)}</span>` : "";
  wrap.innerHTML = `${scoreHTML}${feedbackHTML}`;
  $("chat").appendChild(wrap);
  $("chat").scrollTop = $("chat").scrollHeight;
}

function markCoverageDay(day) {
  if (day === undefined || day === null) return;
  const tags = document.querySelectorAll("#coverageList .coverage-tag");
  tags.forEach(tag => {
    if (tag.textContent.trim() === `D${day}`) tag.classList.add("active");
  });
}

function escapeHTML(value) {
  const div = document.createElement("div");
  div.textContent = value ?? "";
  return div.innerHTML;
}

async function callInterview(payload) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
  });
  if (!response.ok) throw new Error(`API ${response.status}`);
  return response.json();
}

function demoReply() {
  const demo = [
    "Let's start with your architecture. Walk me through how you would build a production RAG pipeline from ingestion to grounded generation.",
    "Good. Now go one level deeper: how would you choose chunking strategy, embedding model, and vector database for a growing enterprise knowledge base?",
    "Suppose retrieval quality is poor even though your embedding model looks reasonable. What would you measure and how would you debug the retrieval layer?",
    "Let's move to agentic systems. When would you choose a single ReAct-style agent versus a multi-agent architecture?",
    "How would you expose your chatbot capabilities through MCP, and what problem does the protocol solve compared with tightly coupled tool integrations?",
    "Imagine your agent is deployed with FastAPI, Docker and Kubernetes. What health checks, failure handling, and scaling considerations would you put in place?",
    "How would you evaluate this system beyond whether the final answer 'looks good'? Give me concrete metrics or test categories.",
    "Final scenario: a production user reports hallucinations and rising latency after traffic doubles. Walk me through your investigation and the changes you would prioritize."
  ];
  return demo[Math.min(state.questionCount - 1, demo.length - 1)];
}

async function startInterview() {
  state.selectedCandidate = selectedCandidate();
  state.sessionId = crypto.randomUUID();
  state.active = true;
  state.questionCount = 0;
  state.coveredDays = new Set();

  $("chat").innerHTML = "";
  $("messageInput").disabled = false;
  $("sendBtn").disabled = false;
  $("sessionLabel").textContent = `Session ${state.sessionId.slice(0, 8)}…`;
  $("connectionLabel").textContent = "Connecting";
  $("interviewTitle").textContent = `Interviewing ${state.selectedCandidate.name}`;
  $("interviewSubtitle").textContent = `${state.selectedCandidate.jobRole} · personalized cohort assessment`;
  $("modePill").textContent = "Live agent";

  addTyping();
  try {
    const result = await callInterview({
      sessionId: state.sessionId,
      candidate: {id: state.selectedCandidate.id}
    });
    removeTyping();
    addMessage("assistant", result.reply);
    markCoverageDay(result.curriculum_day);
    $("connectionLabel").textContent = "Live";
    state.questionCount = result.question_number || 1;
    updateProgress();
    if (result.done) { finishInterview(result); return; }
  } catch (err) {
    removeTyping();
    $("connectionLabel").textContent = "Demo mode";
    $("modePill").textContent = "Local demo";
    addMessage("assistant", "Welcome. Let's begin your interview. I'll adapt the questions to your cohort journey.");
    state.questionCount = 1;
    setTimeout(() => addMessage("assistant", demoReply()), 450);
  }
  updateProgress();
  $("messageInput").focus();
}

async function sendAnswer(event) {
  event.preventDefault();
  if (!state.active) return;
  const input = $("messageInput");
  const message = input.value.trim();
  if (!message) return;

  addMessage("user", message);
  input.value = "";
  input.style.height = "auto";
  $("sendBtn").disabled = true;
  addTyping();

  try {
    const result = await callInterview({sessionId: state.sessionId, message});
    removeTyping();
    addTurnFeedback(result.score, result.feedback);
    addMessage("assistant", result.reply);
    markCoverageDay(result.curriculum_day);
    state.questionCount = result.question_number || (state.questionCount + 1);
    updateProgress();
    if (result.done) finishInterview(result);
  } catch (err) {
    removeTyping();
    state.questionCount++;
    addMessage("assistant", state.questionCount <= 8 ? demoReply() : "Thanks. That concludes the interview. Review the performance report on the right.");
    updateProgress();
    if (state.questionCount >= 8) finishInterview({
      summary: "Demo interview completed. Connect the frontend to your /api/interview backend for real AI-generated scoring and feedback.",
      strengths: ["Engaged with multiple enterprise AI topics.", "Provided architecture-oriented reasoning."],
      gaps: ["Backend integration is not connected in demo mode.", "Structured scoring requires the interview agent response."],
      next: ["Connect POST /api/interview.", "Add server-side adaptive question selection and evaluation."]
    });
  } finally {
    $("sendBtn").disabled = false;
    input.focus();
  }
}

function finishInterview(payload) {
  state.active = false;
  $("messageInput").disabled = true;
  $("sendBtn").disabled = true;
  $("connectionLabel").textContent = "Completed";
  $("interviewTitle").textContent = "Interview complete";
  $("interviewSubtitle").textContent = "Review the structured feedback and next steps.";
  $("feedbackPanel").classList.remove("hidden");

  const p = payload || {};

  // Real backend shape: { final_evaluation: "OVERALL_SCORE: 8.5\n...", score, feedback, ... }
  if (typeof p.final_evaluation === "string") {
    const match = p.final_evaluation.match(/OVERALL_SCORE:\s*([\d.]+)/i);
    $("scoreBadge").textContent = match ? match[1] : (p.score ?? "—");
    $("feedbackContent").innerHTML = `
      <div class="feedback-block"><h3>Final evaluation</h3>
        <div style="font-size:11px;line-height:1.65;white-space:pre-wrap">${escapeHTML(p.final_evaluation)}</div>
      </div>`;
    return;
  }

  // Demo / legacy shape: { summary, strengths[], gaps[], next[] }
  const strength = Array.isArray(p.strengths) ? p.strengths : [];
  const gaps = Array.isArray(p.gaps) ? p.gaps : [];
  const next = Array.isArray(p.next) ? p.next : [];
  const total = strength.length + gaps.length + next.length;
  const score = total ? Math.round((strength.length + next.length * .5) / total * 100) : null;
  $("scoreBadge").textContent = score ? `${score}%` : "—";
  $("feedbackContent").innerHTML = `
    <div class="feedback-block"><h3>Summary</h3><div style="font-size:11px;line-height:1.55">${escapeHTML(p.summary || "No summary returned.")}</div></div>
    <div class="feedback-block"><h3>Strengths</h3><ul>${strength.map(x => `<li>${escapeHTML(x)}</li>`).join("") || "<li>None returned.</li>"}</ul></div>
    <div class="feedback-block"><h3>Gaps</h3><ul>${gaps.map(x => `<li>${escapeHTML(x)}</li>`).join("") || "<li>None returned.</li>"}</ul></div>
    <div class="feedback-block"><h3>Next</h3><ul>${next.map(x => `<li>${escapeHTML(x)}</li>`).join("") || "<li>None returned.</li>"}</ul></div>`;
}

$("candidateSelect").addEventListener("change", () => {
  renderCandidate();
  resetUI();
});
$("startBtn")?.addEventListener("click", startInterview);
$("newInterviewBtn").addEventListener("click", resetUI);
$("composer").addEventListener("submit", sendAnswer);
$("messageInput").addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    $("composer").requestSubmit();
  }
});
$("messageInput").addEventListener("input", e => {
  e.target.style.height = "auto";
  e.target.style.height = `${Math.min(e.target.scrollHeight, 130)}px`;
});
$("themeBtn").addEventListener("click", () => {
  document.body.classList.toggle("dark");
  $("themeBtn").textContent = document.body.classList.contains("dark") ? "☀" : "☾";
});

renderCandidateOptions();
$("candidateSelect").value = "CAND-001";
renderCandidate();
resetUI();