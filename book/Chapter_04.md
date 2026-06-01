# Chapter 4: The Harness Runtime

## 4.1 Orchestration vs. Execution
In the Project Atlas case study, their failure wasn't just the agent—it was that their logic was buried inside the agent's prompts. When the inventory logic failed, they had to rewrite the entire prompt. 

The **Harness Runtime** solves this by separating **Execution (The Model)** from **Orchestration (The Logic).**

## 4.2 The Planner-Worker-Verifier Architecture
Reliability requires a structured, multi-role system:

1.  **The Planner:** Maps high-level intent to a Directed Acyclic Graph (DAG) of steps. It does not execute; it plans.
2.  **The Worker:** Executes a single, sandboxed tool call. It knows nothing of the "Global Intent"—it only knows the specific task at hand.
3.  **The Verifier:** The system’s internal auditor. It evaluates the Worker's output against the Confidence Chain before allowing the Planner to trigger the next step.

## 4.3 State Management & Checkpointing
If a system fails, restarting from scratch is a business loss.
*   **Stateful Context:** The runtime maintains a structured graph of every decision taken.
*   **Checkpointing:** At every node in the plan, the runtime persists the state. If the environment crashes, the agent resumes exactly where it left off.
*   **Non-Blocking Logic:** The runtime supports asynchronous HITL (Human-in-the-Loop) gates, allowing the process to pause and wait for an approval signal without freezing system resources.

> **Key Takeaway:** By turning "agent logic" into a modular, stateful runtime pipeline, we convert brittle, linear scripts into robust, recoverable business workflows.

---
## Chapter Summary
- **Problem:** Tightly coupled agent logic is fragile and unmanageable.
- **Architecture:** Introduced the Planner-Worker-Verifier pattern and stateful execution via check-pointing.
- **Next Step:** Refer to [Chapter 5](Chapter_05.md) to see how this runtime achieves forensic transparency.
