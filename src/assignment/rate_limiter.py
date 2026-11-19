"""Per-user sliding-window rate limiting."""
from __future__ import annotations
from collections import defaultdict, deque
import time
import math
from google.adk.plugins import base_plugin
from google.genai import types

class RateLimitPlugin(base_plugin.BasePlugin):
    def __init__(self, max_requests: int = 10, window_seconds: int = 60):
        super().__init__(name="rate_limiter")
        if max_requests < 1 or window_seconds < 1:
            raise ValueError("Rate limit settings must be positive")
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.user_windows = defaultdict(deque)
        self.blocked_count = 0
        self.total_count = 0

    def _block_response(self, message: str) -> types.Content:
        return types.Content(role="model", parts=[types.Part.from_text(text=message)])

    async def on_user_message_callback(self, *, invocation_context, user_message):
        self.total_count += 1
        user_id = (getattr(invocation_context, "user_id", None)
                   or getattr(getattr(invocation_context, "session", None), "user_id", None)
                   or "anonymous")
        now = time.monotonic()
        window = self.user_windows[user_id]
        while window and window[0] <= now - self.window_seconds:
            window.popleft()
        if len(window) >= self.max_requests:
            self.blocked_count += 1
            wait = math.ceil(self.window_seconds - (now - window[0]))
            return self._block_response(f"Rate limit exceeded. Try again in {wait}s.")
        window.append(now)
        return None
