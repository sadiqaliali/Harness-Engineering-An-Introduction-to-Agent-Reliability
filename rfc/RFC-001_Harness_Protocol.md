# RFC-001: Harness Protocol Specification (v0.1-draft)

**Status:** Draft  
**Author:** OpenHarness AI Steering Council  
**Date:** 2026-05-10  

---

## 1. Abstract
The Harness Protocol defines the foundational semantic layer for agentic interoperability. It ensures that heterogeneous agent systems can exchange state, governance metadata, and trust-verification traces reliably across cloud-native environments.

## 2. Problem Statement
Current agentic architectures suffer from siloed communication, lack of standardized audit trails, and fragmented governance. There is no industry-wide "lingua franca" for multi-agent systems, preventing interoperability and hindering the adoption of reliable Agent Reliability Engineering (ARE) practices.

## 3. Proposed Solution
Implement the Harness Protocol as a **semantic middleware layer** over gRPC/JSON-RPC. It introduces a standardized envelope for every agent-to-agent communication, carrying:
*   **Harness Envelope:** Metadata for tracing, governance, and identity.
*   **Payload:** The functional agent task (tool call, data, or reasoning step).
*   **Governance Header:** Cryptographically signed policy-compliance tokens.

## 4. Technical Design

### 4.1 The Harness Envelope Structure
Every request MUST include the following standard fields:
```json
{
  "header": {
    "protocol_version": "0.1",
    "agent_identity": "UUID",
    "correlation_id": "UUID",
    "governance_token": "Base64(SignedPolicy)"
  },
  "payload": { ... }
}
```

### 4.2 State & Tracing
The protocol mandates that every communication includes an `AFR_Trace_ID`, linking the communication event directly to the **Agent Flight Recorder**. This ensures forensic auditability across distributed agents.

## 5. Alternatives Considered
*   **Direct REST/HTTP:** Rejected; lacks the stateful, bidirectional performance needed for complex reasoning chains.
*   **Pure gRPC without Semantic Layer:** Rejected; gRPC alone does not provide built-in governance, policy enforcement, or agent-identity awareness required for ARE.

## 6. Impact on Architecture
*   **Maintainers:** Must support the envelope parsing in the core Harness Runtime.
*   **Developers:** Must wrap existing RPC clients with a Harness-compatible SDK (the "Harness SDK").

## 7. Open Questions
*   How should we handle large payloads (data-heavy agent tasks) in the envelope without compromising latency?
*   Should the protocol mandate a specific cryptographic scheme for identity, or keep it pluggable?

---

*Comments and feedback should be directed to the OpenHarness AI Steering Council.*
