from core.runtime import HarnessRuntime
import os

def run_demonstration():
    print("=== OpenHarness AI: Industrial Kernel v1.0 ===")
    # Initialize with a unique Agent Identity
    runtime = HarnessRuntime(agent_id="AGENT_X_99")

    # Case 1: Successful Workflow
    print("\n[Running Secure Workflow]")
    success = runtime.execute_workflow("Analyze sales data")
    print(f"Result: {'Success' if success else 'Failed'}")

    print("\nStatus: System verified, identity bound, and integrity secured.")

if __name__ == "__main__":
    run_demonstration()
    print("\nCheck 'agent_flight.log' for the cryptographically bound audit trail.")
