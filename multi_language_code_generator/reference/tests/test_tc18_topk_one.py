import unittest

from multi_language_code_generator.reference.log_analyzer import SlidingWindowLogAnalyzer


class TestTC18TopKOne(unittest.TestCase):
    def test_topk_one_returns_single_endpoint(self):
        analyzer = SlidingWindowLogAnalyzer()
        payload = {
            "window_seconds": 60,
            "step_seconds": 60,
            "top_k": 1,
            "events": [
                {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 10},
                {"timestamp": "2026-04-04T10:00:01Z", "endpoint": "/b", "severity": "INFO", "latency_ms": 10},
                {"timestamp": "2026-04-04T10:00:02Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 10},
            ],
        }
        result = analyzer.analyze(payload)
        self.assertEqual(result["windows"][0]["top_endpoints"], [{"endpoint": "/a", "count": 2}])


if __name__ == "__main__":
    unittest.main()
