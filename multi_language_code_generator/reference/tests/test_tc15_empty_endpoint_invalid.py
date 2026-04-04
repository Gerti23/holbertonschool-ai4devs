import unittest

from multi_language_code_generator.reference.log_analyzer import SlidingWindowLogAnalyzer


class TestTC15EmptyEndpointInvalid(unittest.TestCase):
    def test_empty_endpoint_is_skipped(self):
        analyzer = SlidingWindowLogAnalyzer()
        payload = {
            "window_seconds": 60,
            "step_seconds": 60,
            "top_k": 2,
            "events": [
                {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "", "severity": "INFO", "latency_ms": 10},
            ],
        }
        result = analyzer.analyze(payload)
        self.assertEqual(result["skipped_events"], 1)
        self.assertEqual(result["windows"], [])


if __name__ == "__main__":
    unittest.main()
