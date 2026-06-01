import functools
from dataclasses import dataclass

@dataclass
class AgentTask:
    task_id: str
    objective: str
    status: str = "pending"

def harness_task(func):
    """SDK Decorator: Automatically wraps a function with AFR logging and verification."""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Simplified SDK wrapper for the reference implementation
        return func(self, *args, **kwargs)
    return wrapper
