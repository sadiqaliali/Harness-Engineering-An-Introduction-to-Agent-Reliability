# Lab 03: AFR Forensic Auditing

## Objective
Use the Agent Flight Recorder to reconstruct an agent's reasoning path and verify cryptographic integrity.

## Steps
1. Run a successful workflow using `main.py`.
2. Open `agent_flight.log`.
3. Locate the `previous_hash` and `hash` fields for each entry.
4. Run the cryptographic integrity script:
   ```bash
   $env:PYTHONPATH='.'; python tests/test_cryptographic_integrity.py
   ```
5. Attempt to manually edit a single character in the log file and re-run the script.

## Expected Result
The script should report "100% Integrity" for the original log and "Integrity Breach" for the tampered log, demonstrating the forensic power of the AFR.
