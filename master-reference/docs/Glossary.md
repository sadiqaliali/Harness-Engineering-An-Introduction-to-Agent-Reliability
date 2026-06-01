# Harness Engineering: Glossary of Terms

- **AFR (Agent Flight Recorder):** A cryptographically bound, hash-linked audit trail that captures the reasoning graph and intermediate intent of an AI agent.
- **ARE (Agent Reliability Engineering):** The discipline of applying software reliability principles to autonomous agentic systems.
- **Circuit Breaker:** A safety mechanism that forcibly terminates an agent workflow if confidence scores or safety metrics fall below a defined threshold.
- **Confidence Chain:** A mathematical requirement that every step in an agent's reasoning must be assigned a quantified probability or confidence metric.
- **Harness Kernel:** The foundational reference implementation that provides the runtime, observability, and governance layers for agents.
- **Harness Protocol:** A semantic gRPC-based envelope that standardizes communication between disparate agent frameworks.
- **HRI (Harness Reliability Index):** A quantifiable reputation score for AI agents based on historical compliance and performance.
- **HITL (Human-in-the-Loop):** A design pattern where high-risk or low-confidence agent actions are routed to a human operator for approval.
- **PaC (Policy-as-Code):** The enforcement of safety and compliance rules via declarative code injected directly into the system kernel.
- **Planner-Worker-Verifier:** An architectural pattern that decouples the planning of a task, its execution, and its subsequent verification.
