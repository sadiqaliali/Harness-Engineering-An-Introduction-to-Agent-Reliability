import json
import hashlib
from core.runtime import HarnessRuntime
from core.flight_recorder import FlightRecorder
import os

def calculate_event_hash(event_dict):
    # Create a copy and remove existing hash to recalculate
    e = event_dict.copy()
    if 'hash' in e: del e['hash']
    event_str = json.dumps(e, sort_keys=True)
    return hashlib.sha256(event_str.encode()).hexdigest()

def verify_afr_integrity(log_path):
    print("\n--- Starting Cryptographic Integrity Verification ---")
    with open(log_path, "r") as f:
        logs = [json.loads(line) for line in f]
    
    prev_hash = "0" * 64
    for i, event in enumerate(logs):
        # 1. Verify previous_hash link
        if event['previous_hash'] != prev_hash:
            raise ValueError(f"Integrity Breach at index {i}: Hash mismatch!")
        
        # 2. Verify current hash
        actual_hash = calculate_event_hash(event)
        if event['hash'] != actual_hash:
            raise ValueError(f"Integrity Breach at index {i}: Self-hash mismatch!")
        
        print(f"Event {i} [{event['event_type']}]: Verified.")
        prev_hash = event['hash']
        
    print("--- 100% Integrity Confirmed: Audit Trail Untampered ---\n")

class MaliciousWorker:
    def __init__(self, recorder): self.recorder = recorder
    def execute(self, task):
        if task.task_id == "T2": return "MALICIOUS_DATA"
        return "CLEAN_DATA"

def run_stress_test():
    log_file = "agent_flight.log"
    if os.path.exists(log_file): os.remove(log_file)
    
    runtime = HarnessRuntime()
    runtime.worker = MaliciousWorker(runtime.recorder)
    
    print("Running workflow with expected failure...")
    result = runtime.execute_workflow("High-Security Audit")
    
    # Assert result is False (Circuit Breaker tripped)
    assert result is False, "Failure should have triggered circuit breaker"
    
    # Check if workflow reached the end
    with open(log_file, "r") as f:
        logs = [json.loads(line) for line in f]
        assert not any(l['event_type'] == "WORKFLOW_END" for l in logs), "Workflow should have stopped"

    verify_afr_integrity(log_file)

if __name__ == "__main__":
    run_stress_test()
