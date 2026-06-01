# Lab 01: Initializing the Kernel

## Objective
To deploy a basic Harness-Core MVP and verify it against the integrity suite.

## Instructions
1. Navigate to `/core`.
2. Run `python3 runtime.py` to initialize the Planner-Worker-Verifier.
3. Review `agent_flight.log` to confirm the forensic audit trail is generating.

## Success Criteria
- [ ] Workflow starts and ends correctly.
- [ ] `agent_flight.log` contains valid JSON events.
- [ ] Cryptographic hash chain is intact.
