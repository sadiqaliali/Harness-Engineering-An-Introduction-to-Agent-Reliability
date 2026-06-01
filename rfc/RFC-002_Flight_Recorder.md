# RFC-002: Agent Flight Recorder (AFR) Specification (v0.1-draft)

**Status:** Draft  
**Author:** OpenHarness AI Steering Council  
**Date:** 2026-05-10  

---

## 1. Abstract
The Agent Flight Recorder (AFR) provides the standardized logging and telemetry framework required for forensic observability in agentic systems. It ensures that every reasoning branch, tool call, and state transition is captured in an immutable, replayable format.

## 2. Technical Design

### 2.1 The AFR Event Schema
Each entry in the AFR MUST follow this structure to ensure interop:

```json
{
  "trace_id": "UUID",
  "timestamp": "ISO8601",
  "event_type": "THOUGHT | TOOL_CALL | VERIFIER_CHECK | CIRCUIT_BREAKER",
  "actor_id": "UUID",
  "content": { ... },
  "confidence_metrics": {
    "step_score": 0.0,
    "cumulative_score": 0.0
  },
  "hash": "SHA-256(previous_event_hash + current_content)"
}
```

### 2.2 Storage & Immutability
*   **Tamper-Evidence:** Each record includes a hash of the previous record, creating a cryptographic chain that detects unauthorized log modification.
*   **Persistence:** The AFR MUST be stored in an append-only, high-performance datastore (e.g., ClickHouse, S3-backed event log).

## 3. Impact
This specification enables the "Time-Travel Debugging" mentioned in Chapter 5, allowing developers to replay agent failures with full context.
