import uuid
import time

class SecurityManager:
    """Enterprise-grade Identity: Issues and validates agent session tokens."""
    
    # In production, use a secure vault (e.g., HashiCorp Vault)
    _active_sessions = {}

    @classmethod
    def issue_token(cls, agent_id: str) -> str:
        token = f"HSK_{agent_id}_{uuid.uuid4().hex}"
        cls._active_sessions[token] = {"agent_id": agent_id, "expires": time.time() + 3600}
        return token

    @classmethod
    def validate_request(cls, token: str) -> bool:
        session = cls._active_sessions.get(token)
        if session and session['expires'] > time.time():
            return True
        return False
