# RFC-003: Governance Policy-as-Code (PaC) Schema (v0.1-draft)

**Status:** Draft  
**Author:** OpenHarness AI Steering Council  
**Date:** 2026-05-10  

---

## 1. Abstract
The Governance Policy-as-Code (PaC) schema provides a standardized, YAML-based configuration format for defining agent safety boundaries, permissions, and compliance rules.

## 2. Policy Schema Definition
Policies are defined at the agent or workflow level.

```yaml
policy_metadata:
  version: "0.1"
  scope: "data-analysis-agent"

constraints:
  - id: "PII_REDACTION"
    trigger: "data_access"
    action: "BLOCK_AND_FLAG"
    threshold: 0.85 # Confidence threshold

circuit_breaker:
  max_iterations: 5
  on_trigger: "HALT_AND_LOG"
  alert_channel: "admin-ops"
```

## 3. Enforcement Logic
*   **Compile-time:** Policies are parsed by the Harness Runtime upon agent initialization.
*   **Run-time:** The Runtime evaluates these rules against the `Agent Flight Recorder` events in real-time, triggering actions (BLOCK/HALT/ALERT) if rules are violated.

## 4. Impact
This decouples safety logic from the agent's prompts, ensuring that compliance rules are immutable and externally verifiable.
