from core.runtime import HarnessRuntime
from core.flight_recorder import FlightRecorder
import os

class MockWorker:
    def __init__(self, recorder: FlightRecorder):
        self.recorder = recorder

    def execute(self, task):
        # SIMULATION: Worker tries to leak sensitive PII
        if task.task_id == "T2":
            return "LEAKED_PII_DATA"
        return f"Completed: {task.objective}"

def test_governance_failure_trapping():
    """
    Test that the Harness Runtime detects malicious/failed output,
    triggers the circuit breaker, and records the failure in the Flight Recorder.
    """
    runtime = HarnessRuntime()
    # Replace the worker with our malicious mock
    runtime.worker = MockWorker(runtime.recorder)
    
    # Run the workflow
    # T1 will succeed, T2 will fail verification (due to "LEAKED_PII_DATA")
    result = runtime.execute_workflow("Secure Analysis")
    
    # Assert circuit breaker was triggered
    assert result is False
    
    # Verify the failure is in the Flight Recorder
    with open("agent_flight.log", "r") as f:
        logs = f.readlines()
        
    assert any("CIRCUIT_BREAKER" in log for log in logs)
    print("Integration Test Passed: Circuit Breaker triggered and failure recorded.")

if __name__ == "__main__":
    # Clean previous logs
    if os.path.exists("agent_flight.log"):
        os.remove("agent_flight.log")
        
    test_governance_failure_trapping()
