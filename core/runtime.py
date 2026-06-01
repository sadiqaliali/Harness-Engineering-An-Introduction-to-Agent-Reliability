import functools
from typing import Dict, Any, List
from core.base import AgentTask, harness_task
from core.flight_recorder import FlightRecorder
from core.verifier import SecurityVerifier, IntegrityVerifier, PerformanceVerifier
from services.auth.security_manager import SecurityManager
from core.planner import Planner
from core.worker import Worker

class HarnessRuntime:
    def __init__(self, agent_id: str = "AGENT_DEFAULT"):
        self.agent_id = agent_id
        self.token = SecurityManager.issue_token(agent_id)
        self.recorder = FlightRecorder()
        self.planner = Planner(self.recorder)
        self.worker = Worker(self.recorder)
        self.jury = [SecurityVerifier(), IntegrityVerifier(), PerformanceVerifier()]

    def execute_workflow(self, objective: str):
        # Identity Verification check before starting
        if not SecurityManager.validate_request(self.token):
            raise PermissionError("Identity verification failed!")
            
        self.recorder.record("WORKFLOW_START", self.agent_id, {"objective": objective})
        plan = self.planner.create_plan(objective)
        
        for task in plan:
            result = self.worker.execute(task)
            
            # Jury Consensus
            verdict = sum([v.verify(task, result) for v in self.jury])
            
            # Senior Audit Fix: Stricter industrial safety thresholds
            if 1.5 <= verdict < 2.5:
                self.recorder.record("HITL_REQUESTED", self.agent_id, {"task_id": task.task_id, "verdict": verdict})
                print(f"\n[!] HITL Required for Task {task.task_id} (Verdict: {verdict:.2f})")
                # Simulate human approval
                user_approval = "YES" 
                if user_approval != "YES":
                    self.recorder.record("HITL_REJECTED", self.agent_id, {"task_id": task.task_id})
                    return False
                self.recorder.record("HITL_APPROVED", self.agent_id, {"task_id": task.task_id})

            elif verdict < 1.5:
                self.recorder.record("CIRCUIT_BREAKER", self.agent_id, {"task_id": task.task_id, "verdict": verdict})
                return False
        
        self.recorder.record("WORKFLOW_END", self.agent_id, {"status": "success"})
        return True
