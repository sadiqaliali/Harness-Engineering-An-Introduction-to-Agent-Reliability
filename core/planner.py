from typing import List
from core.flight_recorder import FlightRecorder
from core.base import AgentTask

class Planner:
    """The Architect: Decomposes objectives into verifiable tasks."""
    def __init__(self, recorder: FlightRecorder):
        self.recorder = recorder

    def create_plan(self, objective: str) -> List[AgentTask]:
        # Simple heuristic decomposition
        tasks = []
        if "data" in objective.lower():
            tasks = [
                AgentTask("T1", "Extract data from source"),
                AgentTask("T2", "Validate data integrity"),
                AgentTask("T3", "Format data for reporting")
            ]
        else:
            tasks = [
                AgentTask("T1", "Analyze objective constraints"),
                AgentTask("T2", "Execute core logic"),
                AgentTask("T3", "Verify outcome")
            ]
            
        self.recorder.record("PLAN_CREATED", "PLANNER", {
            "objective": objective,
            "tasks": [t.task_id for t in tasks]
        })
        return tasks
