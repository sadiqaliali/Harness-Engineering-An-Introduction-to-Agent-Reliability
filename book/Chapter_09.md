# Chapter 9: Harness-Core Reference MVP

## 9.1 From Theory to Kernel
The Harness-Core MVP is the reference implementation of our architecture. It transforms the book's abstract patterns into a concrete, deployable system.

## 9.2 The "Harness-Core" Implementation
The MVP implements the Planner-Worker-Verifier pattern using modular, decoupled components.
*   **The Orchestrator:** Manages the task lifecycle and state transitions.
*   **The SDK:** A set of Python/Go decorators that wrap tool calls, automatically injecting AFR logging and Policy Engine calls.
*   **The Policy Engine:** A YAML-based governance system that evaluates actions against enterprise-level rules.

## 9.3 Validating the Kernel
How do we prove it works?
1.  **Forensic Proof:** Every action is hash-linked in the Flight Recorder. We can cryptographically prove the path taken by the agent.
2.  **Governance Proof:** Attempting a "malicious" action triggers the Policy Engine’s circuit breaker, proving that governance is enforced at the kernel level, not just the prompt level.

## 9.4 A Note on Extensibility
The MVP is designed to be the *starter kit*. Developers can swap our simple "Jury" verifier for their own complex model-based verifiers, or swap our local file-based AFR for a cloud-native event-bus (Kafka/NATS). The contract—the Harness Protocol—remains the constant foundation.

> **Key Takeaway:** The Reference MVP is the "Ground Truth." It demonstrates that Harness Engineering is a repeatable, measurable, and industrial-grade framework for AI reliability.

---
## Chapter Summary
- **Problem:** Theory must be grounded in a repeatable reference implementation.
- **Architecture:** Introduced the Harness-Core MVP (Planner-Worker-Verifier) with integrated observability.
- **Next Step:** Refer to [Chapter 10](Chapter_10.md) for future research frontiers in ARE.
