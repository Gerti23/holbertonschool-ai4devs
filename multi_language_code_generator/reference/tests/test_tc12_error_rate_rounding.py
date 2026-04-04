import unittest

from multi_language_code_generator.reference.log_analyzer import SlidingWindowLogAnalyzer


class TestTC12ErrorRateRounding(unittest.TestCase):
    def test_error_rate_rounding(self):
        analyzer = SlidingWindowLogAnalyzer()
        payload = {
            "window_seconds": 60,
            "step_seconds": 60,
            "top_k": 2,
            "events": [
                {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "ERROR", "latency_ms": 1},
                {"timestamp": "2026-04-04T10:00:01Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 2},
                {"timestamp": "2026-04-04T10:00:02Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 3},
            ],
        }
        result = analyzer.analyze(payload)
        self.assertEqual(result["windows"][0]["error_rate"], 0.3333)


if __name__ == "__main__":
    unittest.main()
