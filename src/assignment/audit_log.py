"""Audit observer: correlate requests, redact sensitive text and export JSON."""
from __future__ import annotations
import json
import time
import re
from datetime import datetime, timezone
from pathlib import Path

def default_audit_log_path() -> str:
    return str(Path(__file__).resolve().parents[2] / "outputs" / "audit_log.json")

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def redact_for_log(text: str) -> str:
    from guardrails.output_guardrails import content_filter
    from core.config import DEMO_SECRETS
    for secret in sorted(filter(None, DEMO_SECRETS), key=len, reverse=True):
        text = re.sub(re.escape(secret), "[REDACTED]", text, flags=re.I)
    return content_filter(text)["redacted"]

class AuditLogPlugin:
    def __init__(self):
        self.name = "audit_log"
        self.logs: list[dict] = []
        self._open: dict[tuple[str, str], dict] = {}

    def record_input(self, *, user_id: str, text: str, request_id: str | None = None):
        key = (user_id, request_id or user_id)
        self._open[key] = {"timestamp": utc_now_iso(), "input": redact_for_log(text), "start": time.monotonic()}

    def record_output(self, *, user_id: str, text: str, blocked: bool = False,
                      layer: str | None = None, request_id: str | None = None):
        key = (user_id, request_id or user_id)
        entry = self._open.pop(key, None)
        self.logs.append({"request_id": request_id or user_id, "user_id": user_id,
                          "timestamp": entry["timestamp"] if entry else utc_now_iso(),
                          "input": entry["input"] if entry else "",
                          "output": redact_for_log(text), "blocked": blocked, "layer": layer,
                          "latency_ms": round((time.monotonic() - entry["start"]) * 1000, 3) if entry else 0.0})

    def export_json(self, filepath: str | None = None):
        path = Path(filepath or default_audit_log_path())
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.logs, ensure_ascii=False, indent=2), encoding="utf-8")
