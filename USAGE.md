# Harness Engineering: Usage Guide

## 1. Quick Start
The Harness Kernel is designed to be easily integrated into any agentic workflow.

### Running a Secure Workflow
```python
from core.runtime import HarnessRuntime

# Initialize the industrial kernel
runtime = HarnessRuntime(agent_id="ALPHA_REPORTER")

# Execute an objective through the Planner-Worker-Verifier loop
success = runtime.execute_workflow("Analyze Q1 financial data for anomalies")

if success:
    print("Workflow completed and verified.")
else:
    print("Circuit breaker triggered! Check agent_flight.log for forensic data.")
```

## 2. Using the SDK Decorator
You can wrap your own worker functions using the `@harness_task` decorator:

```python
from core.runtime import harness_task

class CustomWorker:
    @harness_task
    def process_data(self, data):
        # Your custom logic here
        return f"Processed: {data}"
```

## 3. Running Integrity Tests
Verification is a core pillar of ARE. Always run the integrity tests before deployment:

```bash
# Set PYTHONPATH to the current directory
$env:PYTHONPATH='.'

# Run the integration and cryptographic tests
python tests/test_integrity.py
python tests/test_cryptographic_integrity.py
```

## 4. Policy Configuration
Governance rules are defined in `services/governance/policy.yaml`. You can adjust thresholds for PII detection, iteration limits, and circuit breaker behavior there.
