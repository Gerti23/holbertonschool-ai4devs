import unittest

from multi_language_code_generator.reference.log_analyzer import SlidingWindowLogAnalyzer


class TestTC11WindowCount(unittest.TestCase):
    def test_window_count_with_step(self):
        analyzer = SlidingWindowLogAnalyzer()
        payload = {
            "window_seconds": 60,
            "step_seconds": 30,
            "top_k": 2,
            "events": [
                {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 10},
                {"timestamp": "2026-04-04T10:01:00Z", "endpoint": "/b", "severity": "INFO", "latency_ms": 20},
            ],
        }
        result = analyzer.analyze(payload)
        self.assertGreaterEqual(len(result["windows"]), 3)


if __name__ == "__main__":
    unittest.main()
