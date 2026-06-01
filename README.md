<p align="center">
  <img src="assets/Cover image.png" width="600" alt="Harness Engineering Cover">
</p>

# Harness Engineering: Industrial Infrastructure for AI Agents

**Build the harness, not just the horse.**

Harness Engineering is the discipline of building operational infrastructure for reliable, governable, and observable AI agents. This repository contains the **Harness Kernel**, a reference implementation for Agent Reliability Engineering (ARE).

> **Industry Formula (2026):** `Agent = Model + Harness`

## 🚀 The Production Wall
In 2026, 88% of AI agent projects fail to reach production. Why? Because agents are treated as "black boxes" without the necessary infrastructure to manage reasoning drift, orchestration chaos, and the observability void.

**Harness Engineering solves this by moving governance, reliability, and observability from prompts into a hardened System Kernel.**

## ⚖️ Why Harness Engineering? (Competitive Landscape)

| Feature | LangGraph / CrewAI | OpenTelemetry | **Harness Engineering (ARE)** |
| :--- | :---: | :---: | :---: |
| **Orchestration** | ✅ Full | ❌ None | ✅ Kernel-Level |
| **Observability** | ⚠️ Basic | ✅ Full | ✅ Forensic (AFR) |
| **Audit Integrity** | ❌ None | ❌ None | ✅ Cryptographic SHA-256 |
| **Governance** | ⚠️ Prompt-Based | ❌ None | ✅ Policy-as-Code (PaC) |
| **Reliability Math** | ❌ None | ❌ None | ✅ SRS / CC Formulas |
| **Maturity Model** | ❌ None | ❌ None | ✅ HRMM (L1-L5) |

**Positioning Statement:** While tools like LangGraph focus on *how* an agent talks, Harness Engineering focuses on the *industrial safety* of that conversation. We provide the only formalized, open-source discipline combining reliability math with cryptographic audit trails.

## 📖 Interactive Reading Guide
Explore the book chapter-by-chapter for the best experience:

- **[Front Matter: Title & Preface](book/TITLE_PAGE.md)**
- **[Chapter 01: What is Harness Engineering?](book/Chapter_01.md)**
- **[Chapter 02: Failure Modes of Agentic Systems](book/Chapter_02.md)**
- **[Chapter 03: Agent Reliability Engineering (ARE)](book/Chapter_03.md)**
- **[Chapter 04: The Harness Runtime](book/Chapter_04.md)**
- **[Chapter 05: AI Observability & The Flight Recorder](book/Chapter_05.md)**
- **[Chapter 06: The AI Governance Layer](book/Chapter_06.md)**
- **[Chapter 07: Cloud-Native Agentic Infrastructure](book/Chapter_07.md)**
- **[Chapter 08: The Harness Protocol](book/Chapter_08.md)**
- **[Chapter 09: Harness-Core Reference MVP](book/Chapter_09.md)**
- **[Chapter 10: Future Research Frontiers](book/Chapter_10.md)**
- **[Chapter 11: The Future of Harness Engineering](book/Chapter_11.md)**

*Download the complete master manuscript here: **[Harness-Engineering-An-Introduction-to-Agent-Reliability.md](Harness-Engineering-An-Introduction-to-Agent-Reliability.md)***

## 📈 Harness Reliability Maturity Model (HRMM)
This project helps organizations move through the five levels of agentic maturity:
- **L1 (Ad-hoc):** Single-model prompts with manual verification.
- **L2 (Observed):** Basic logging and error tracking.
- **L3 (Governed):** Policy-as-Code boundaries and runtime enforcement.
- **L4 (Forensic):** Cryptographically linked audit trails (AFR).
- **L5 (Industrial):** Autonomous consensus (Jury) and stochastic reliability (SRS).

## 🛠️ Core Architecture
- **Harness Runtime:** Decouples orchestration (Planner-Worker-Verifier) from model inference.
- **Agent Flight Recorder (AFR):** Forensic audit logs with cryptographic hash-linking for AI decision-tracing.
- **Governance Kernel:** Policy-as-Code (PaC) to enforce safety boundaries at the runtime level.
- **Harness Protocol:** A semantic gRPC-based middleware ensuring global agent interoperability.

## 🏁 Getting Started
### 1. Installation
```bash
git clone https://github.com/sadiqaliali/Harness-Engineering-An-Introduction-to-Agent-Reliability.git
cd Harness-Engineering-An-Introduction-to-Agent-Reliability
pip install -r requirements.txt
```

### 2. Run the Demo
```bash
python main.py
```

### 3. Run Tests
```bash
$env:PYTHONPATH='.'; python tests/test_integrity.py
```

## 📜 License
Licensed under MIT. Harness Engineering is an evolving research discipline.
