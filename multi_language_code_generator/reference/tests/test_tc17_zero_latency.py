import unittest

from multi_language_code_generator.reference.log_analyzer import SlidingWindowLogAnalyzer


class TestTC17ZeroLatency(unittest.TestCase):
    def test_zero_latency_allowed(self):
        analyzer = SlidingWindowLogAnalyzer()
        payload = {
            "window_seconds": 60,
            "step_seconds": 60,
            "top_k": 1,
            "events": [
                {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 0},
            ],
        }
        result = analyzer.analyze(payload)
        self.assertEqual(result["windows"][0]["p95_latency_ms"], 0)


if __name__ == "__main__":
    unittest.main()
