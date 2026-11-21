import threading
import unittest
from unittest.mock import patch

from rate_limiter import RateLimiter

KEY = ("alice", "/v1/chat")


class FakeClockTests(unittest.TestCase):
    def setUp(self):
        self.now = 0.0
        patcher = patch("rate_limiter.time.monotonic", lambda: self.now)
        patcher.start()
        self.addCleanup(patcher.stop)

    def check_at(self, seconds, limiter, params):
        self.now = seconds
        return limiter.check(*KEY, *params)

    def assert_decision(self, decision, allowed, remaining, reset_ms):
        self.assertEqual(decision[:2], (allowed, remaining))
        self.assertIs(type(decision[2]), int)
        self.assertAlmostEqual(decision[2], reset_ms, delta=1)

    def test_policy_a_exact_limit_and_rejection(self):
        limiter = RateLimiter("policy_a")
        params = (2, 10_000, 0, 0)
        self.assert_decision(self.check_at(0, limiter, params), True, 1, 10_000)
        self.assert_decision(self.check_at(3, limiter, params), True, 0, 7_000)
        self.assert_decision(self.check_at(3.5, limiter, params), False, 0, 6_500)
        self.assert_decision(self.check_at(10, limiter, params), True, 0, 3_000)

    def test_policy_a_recovery_after_expiry(self):
        limiter = RateLimiter("policy_a")
        params = (2, 120, 0, 0)
        self.check_at(0, limiter, params)
        self.check_at(0, limiter, params)
        self.assert_decision(self.check_at(0.14, limiter, params), True, 1, 120)

    def test_policy_b_initial_burst(self):
        limiter = RateLimiter("policy_b")
        params = (0, 0, 3, 0.5)
        for remaining in (2, 1, 0):
            self.assert_decision(self.check_at(0, limiter, params), True, remaining, 0)
        self.assert_decision(self.check_at(0, limiter, params), False, 0, 2_000)

    def test_policy_b_partial_refill(self):
        limiter = RateLimiter("policy_b")
        params = (0, 0, 3, 0.5)
        for _ in range(3):
            self.check_at(0, limiter, params)
        self.assert_decision(self.check_at(1.2, limiter, params), False, 0, 800)


class ConcurrencyTests(unittest.TestCase):
    def test_same_key_burst_allows_exactly_limit(self):
        threads_count, limit = 50, 10
        cases = (
            ("policy_a", (limit, 60_000, 0, 0)),
            ("policy_b", (0, 0, limit, 0)),
        )
        for strategy, params in cases:
            with self.subTest(strategy=strategy):
                limiter = RateLimiter(strategy)
                barrier = threading.Barrier(threads_count)
                results = []

                def worker():
                    barrier.wait()
                    results.append(limiter.check(*KEY, *params)[0])

                threads = [threading.Thread(target=worker) for _ in range(threads_count)]
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()

                self.assertEqual(results.count(True), limit)
                self.assertEqual(
                    limiter.stats(),
                    {
                        "strategy": strategy,
                        "total_allowed": limit,
                        "total_rejected": threads_count - limit,
                        "active_keys": 1,
                    },
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
