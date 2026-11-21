import time
import threading
from collections import deque
from typing import Deque, Dict, NamedTuple, Tuple, TypedDict

Key = Tuple[str, str]
Decision = Tuple[bool, int, int]


class StatsDict(TypedDict):
    strategy: str
    total_allowed: int
    total_rejected: int
    active_keys: int


class TokenBucket(NamedTuple):
    tokens: float
    refilled_at_ms: float


class RateLimiter:
    def __init__(self, strategy: str = "policy_a"):
        if strategy not in ("policy_a", "policy_b"):
            raise ValueError(f"Unknown strategy: {strategy}")

        self.strategy = strategy
        self._lock = threading.Lock()

        self._windows: Dict[Key, Deque[float]] = {}
        self._buckets: Dict[Key, TokenBucket] = {}

        self._total_allowed = 0
        self._total_rejected = 0

    def check(
        self,
        client_id: str,
        endpoint: str,
        limit: int,
        window_ms: int,
        capacity: int,
        refill_rate: float,
    ) -> Decision:
        """
        Run the configured policy and return (allowed, remaining, reset_after_ms).

        Policy A uses: limit, window_ms
        Policy B uses: capacity, refill_rate

        remaining:
            Remaining capacity after the current decision.

        reset_after_ms:
            Milliseconds until capacity becomes available again.
        """
        with self._lock:
            if self.strategy == "policy_a":
                result = self.policy_a_limit(client_id, endpoint, limit, window_ms)
            else:
                result = self.policy_b_limit(client_id, endpoint, capacity, refill_rate)

            if result[0]:
                self._total_allowed += 1
            else:
                self._total_rejected += 1

            return result

    def policy_a_limit(
        self,
        client_id: str,
        endpoint: str,
        limit: int,
        window_ms: int,
    ) -> Decision:
        """
        Policy A:
        For each (client_id, endpoint), allow at most `limit` requests during
        the most recent `window_ms` milliseconds.
        """
        now_ms = time.monotonic() * 1000
        accepted_at_ms = self._windows.setdefault((client_id, endpoint), deque())
        while accepted_at_ms and now_ms - accepted_at_ms[0] >= window_ms:
            accepted_at_ms.popleft()

        allowed = len(accepted_at_ms) < limit
        if allowed:
            accepted_at_ms.append(now_ms)

        remaining = max(0, limit - len(accepted_at_ms)) if allowed else 0
        reset_after_ms = int(accepted_at_ms[0] + window_ms - now_ms)
        return allowed, remaining, reset_after_ms

    def policy_b_limit(
        self,
        client_id: str,
        endpoint: str,
        capacity: int,
        refill_rate: float,
    ) -> Decision:
        """
        Policy B:
        For each (client_id, endpoint), maintain a request budget with maximum
        size `capacity`. The budget increases over time at `refill_rate` units
        per second, up to `capacity`. Each accepted request consumes 1 unit.
        """
        now_ms = time.monotonic() * 1000
        key = (client_id, endpoint)
        bucket = self._buckets.get(key, TokenBucket(capacity, now_ms))
        elapsed_s = (now_ms - bucket.refilled_at_ms) / 1000
        tokens = min(capacity, bucket.tokens + elapsed_s * refill_rate)

        allowed = tokens >= 1
        if allowed:
            tokens -= 1
        self._buckets[key] = TokenBucket(tokens, now_ms)

        if allowed:
            return True, int(tokens), 0
        reset_after_ms = int((1 - tokens) / refill_rate * 1000) if refill_rate > 0 else 0
        return False, 0, reset_after_ms

    def stats(self) -> StatsDict:
        """
        Return aggregate limiter statistics.

        active_keys counts tracked (client_id, endpoint) entries for the active
        policy state.
        """
        with self._lock:
            return {
                "strategy": self.strategy,
                "total_allowed": self._total_allowed,
                "total_rejected": self._total_rejected,
                "active_keys": len(self._windows) + len(self._buckets),
            }
