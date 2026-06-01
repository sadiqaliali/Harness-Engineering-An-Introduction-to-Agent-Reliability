import json
import uuid
import datetime
import hashlib
from typing import Dict, Any

class FlightRecorder:
    """The Agent Flight Recorder: Forensic audit trail for agent actions."""
    def __init__(self, log_path: str = "agent_flight.log"):
        self.log_path = log_path
        self.last_hash = "0" * 64

    def record(self, event_type: str, actor_id: str, content: Dict[str, Any], confidence: float = 1.0):
        event = {
            "trace_id": str(uuid.uuid4()),
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "event_type": event_type,
            "actor_id": actor_id,
            "content": content,
            "confidence_metrics": {"step_score": confidence},
            "previous_hash": self.last_hash
        }
        
        # Calculate new hash
        event_str = json.dumps(event, sort_keys=True)
        self.last_hash = hashlib.sha256(event_str.encode()).hexdigest()
        event["hash"] = self.last_hash
        
        # Append to log
        with open(self.log_path, "a") as f:
            f.write(json.dumps(event) + "\n")
        
        print(f"AFR: Recorded {event_type} (Hash: {self.last_hash[:8]}...)")
