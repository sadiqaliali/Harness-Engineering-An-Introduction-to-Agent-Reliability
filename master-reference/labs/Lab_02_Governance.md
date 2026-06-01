# Lab 02: Governance Policy & Circuit Breakers

## Objective
Configure the Harness Governance Engine to detect and block malicious PII leaks.

## Steps
1. Open `services/governance/policy.yaml`.
2. Set the `pii_redaction` threshold to `0.95` for strict enforcement.
3. Modify the `MockWorker` in `tests/test_integrity.py` to return a string containing "SSN: 000-00-0000".
4. Run the test:
   ```bash
   $env:PYTHONPATH='.'; python tests/test_integrity.py
   ```
5. Observe the `CIRCUIT_BREAKER` event in `agent_flight.log`.

## Expected Result
The workflow should terminate immediately when the PII pattern is detected, preventing the data from reaching the final output.
