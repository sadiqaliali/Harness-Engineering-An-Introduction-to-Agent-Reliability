from typing import Any
from core.flight_recorder import FlightRecorder
from core.base import harness_task

class Worker:
    """The Executor: Performs the actual computational tasks."""
    def __init__(self, recorder: FlightRecorder):
        self.recorder = recorder

    @harness_task
    def execute(self, task) -> Any:
        # Simulate execution logic
        # In a real system, this would call model APIs or local tools
        result = f"Completed: {task.objective}"
        
        self.recorder.record("TASK_EXECUTED", "WORKER", {
            "task_id": task.task_id, 
            "objective": task.objective,
            "result": result
        })
        return result
