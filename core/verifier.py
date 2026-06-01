from typing import List, Any
from abc import ABC, abstractmethod

class Verifier(ABC):
    @abstractmethod
    def verify(self, task, result) -> float:
        pass

class SecurityVerifier(Verifier):
    """Enforces safety and security boundaries on agent outputs."""
    def verify(self, task, result) -> float:
        # Detect malicious patterns or data leaks
        blacklist = ["MALICIOUS", "PII", "SECRET_KEY", "LEAKED"]
        for pattern in blacklist:
            if pattern in str(result).upper():
                return 0.0
        return 1.0

class IntegrityVerifier(Verifier):
    """Checks if the result aligns with the expected task objective."""
    def verify(self, task, result) -> float:
        # In a real system, this might use a small model to check semantic alignment
        # Here we check for execution confirmation
        if "Completed:" in str(result):
            return 1.0
        return 0.0

class PerformanceVerifier(Verifier):
    """Placeholder for latency and token-usage verification."""
    def verify(self, task, result) -> float:
        # Currently defaults to passing
        return 1.0
