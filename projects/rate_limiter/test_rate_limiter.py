"""Public unit tests. They call RateLimiter directly, so no server is needed."""

import sys
import unittest

from rate_limiter import RateLimiter


class PublicTests(unittest.TestCase):
    def assert_decision(
        self, decision, allowed, remaining, minimum_reset_ms, maximum_reset_ms
    ):
        actual_allowed, actual_remaining, actual_reset_ms = decision
        self.assertEqual(actual_allowed, allowed)
        self.assertEqual(actual_remaining, remaining)
        self.assertIs(type(actual_reset_ms), int)
        self.assertTrue(
            minimum_reset_ms <= actual_reset_ms <= maximum_reset_ms,
            f"reset {actual_reset_ms} outside [{minimum_reset_ms},{maximum_reset_ms}]",
        )

    def assert_stats(self, limiter, strategy, total_allowed, total_rejected, active_keys):
        self.assertEqual(
            limiter.stats(),
            {
                "strategy": strategy,
                "total_allowed": total_allowed,
                "total_rejected": total_rejected,
                "active_keys": active_keys,
            },
        )

    def test_exact_limit_then_reject(self):
        """Allows requests up to the sliding-window limit, then rejects the next one."""
        limiter = RateLimiter("policy_a")
        first = limiter.check("alice", "/v1/chat", 2, 500, 0, 0)
        second = limiter.check("alice", "/v1/chat", 2, 500, 0, 0)
        third = limiter.check("alice", "/v1/chat", 2, 500, 0, 0)
        self.assert_decision(first, True, 1, 1, 500)
        self.assert_decision(second, True, 0, 1, 500)
        self.assert_decision(third, False, 0, 1, 500)

    def test_initial_burst_then_reject(self):
        """Allows an initial token-bucket burst up to capacity, then rejects."""
        limiter = RateLimiter("policy_b")
        first = limiter.check("alice", "/v1/chat", 0, 0, 3, 0.5)
        second = limiter.check("alice", "/v1/chat", 0, 0, 3, 0.5)
        third = limiter.check("alice", "/v1/chat", 0, 0, 3, 0.5)
        fourth = limiter.check("alice", "/v1/chat", 0, 0, 3, 0.5)
        self.assert_decision(first, True, 2, 0, 0)
        self.assert_decision(second, True, 1, 0, 0)
        self.assert_decision(third, True, 0, 0, 0)
        self.assert_decision(fourth, False, 0, 1700, 2000)

    def test_client_isolation(self):
        """Keeps state separate for different clients."""
        limiter = RateLimiter("policy_a")
        limiter.check("alice", "/v1/chat", 1, 500, 0, 0)
        second = limiter.check("alice", "/v1/chat", 1, 500, 0, 0)
        third = limiter.check("bob", "/v1/chat", 1, 500, 0, 0)
        self.assert_decision(second, False, 0, 1, 500)
        self.assert_decision(third, True, 0, 1, 500)

    def test_endpoint_isolation(self):
        """Keeps state separate for different endpoints."""
        limiter = RateLimiter("policy_b")
        limiter.check("alice", "/v1/chat", 2, 500, 1, 0)
        second = limiter.check("alice", "/v1/chat", 2, 500, 1, 0)
        third = limiter.check("alice", "/v1/complete", 2, 500, 1, 0)
        self.assert_decision(second, False, 0, 0, sys.maxsize)
        self.assert_decision(third, True, 0, 0, 0)

    def test_stats_policy_a(self):
        """Reports accurate acceptance, rejection and active-key totals for policy_a."""
        limiter = RateLimiter("policy_a")
        self.assert_stats(limiter, "policy_a", 0, 0, 0)
        limiter.check("alice", "/v1/chat", 2, 500, 2, 0)
        limiter.check("alice", "/v1/chat", 2, 500, 2, 0)
        limiter.check("alice", "/v1/chat", 2, 500, 2, 0)
        limiter.check("bob", "/v1/chat", 2, 500, 2, 0)
        self.assert_stats(limiter, "policy_a", 3, 1, 2)

    def test_stats_policy_b(self):
        """Reports accurate acceptance, rejection and active-key totals for policy_b."""
        limiter = RateLimiter("policy_b")
        self.assert_stats(limiter, "policy_b", 0, 0, 0)
        limiter.check("alice", "/v1/chat", 2, 500, 2, 0)
        limiter.check("alice", "/v1/chat", 2, 500, 2, 0)
        limiter.check("alice", "/v1/chat", 2, 500, 2, 0)
        limiter.check("bob", "/v1/chat", 2, 500, 2, 0)
        self.assert_stats(limiter, "policy_b", 3, 1, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
