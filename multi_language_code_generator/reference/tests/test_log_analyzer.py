import unittest

from multi_language_code_generator.reference.log_analyzer import SlidingWindowLogAnalyzer


class TestSlidingWindowLogAnalyzer(unittest.TestCase):
    def setUp(self) -> None:
        self.analyzer = SlidingWindowLogAnalyzer()

    def _payload(self, events, window_seconds=60, step_seconds=30, top_k=2):
        return {
            "window_seconds": window_seconds,
            "step_seconds": step_seconds,
            "top_k": top_k,
            "events": events,
        }

    def test_tc01_basic_mixed_severities(self):
        events = [
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 100},
            {"timestamp": "2026-04-04T10:00:10Z", "endpoint": "/a", "severity": "ERROR", "latency_ms": 120},
            {"timestamp": "2026-04-04T10:00:20Z", "endpoint": "/b", "severity": "INFO", "latency_ms": 200},
            {"timestamp": "2026-04-04T10:00:30Z", "endpoint": "/c", "severity": "WARN", "latency_ms": 310},
        ]
        result = self.analyzer.analyze(self._payload(events, window_seconds=60, step_seconds=60, top_k=2))
        window = result["windows"][0]
        self.assertEqual(window["total_events"], 4)
        self.assertEqual(window["error_events"], 1)
        self.assertEqual(window["error_rate"], 0.25)
        self.assertEqual(window["p95_latency_ms"], 310)
        self.assertEqual(window["top_endpoints"], [{"endpoint": "/a", "count": 2}, {"endpoint": "/b", "count": 1}])

    def test_tc02_empty_event_list(self):
        result = self.analyzer.analyze(self._payload([]))
        self.assertEqual(result["skipped_events"], 0)
        self.assertEqual(result["windows"], [])

    def test_tc03_invalid_records_skipped(self):
        events = [
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 50},
            {"timestamp": "2026-04-04T10:00:05Z", "endpoint": "/b", "severity": "ERROR", "latency_ms": 100},
            {"timestamp": "2026-04-04T10:00:10Z", "endpoint": "/c", "severity": "WARN", "latency_ms": 120},
            {"timestamp": "2026-04-04T10:00:11Z", "endpoint": "/x", "severity": "INFO", "latency_ms": -1},
            {"timestamp": "2026-04-04T10:00:12Z", "endpoint": "/y", "severity": "TRACE", "latency_ms": 10},
        ]
        result = self.analyzer.analyze(self._payload(events, window_seconds=60, step_seconds=60))
        self.assertEqual(result["skipped_events"], 2)
        self.assertEqual(result["windows"][0]["total_events"], 3)

    def test_tc04_boundary_correctness(self):
        events = [
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 10},
            {"timestamp": "2026-04-04T10:00:59Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 20},
            {"timestamp": "2026-04-04T10:01:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 30},
        ]
        result = self.analyzer.analyze(self._payload(events, window_seconds=60, step_seconds=60))
        self.assertEqual(result["windows"][0]["total_events"], 2)
        self.assertEqual(result["windows"][1]["total_events"], 1)

    def test_tc05_top_k_tie_break(self):
        events = [
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/b", "severity": "INFO", "latency_ms": 10},
            {"timestamp": "2026-04-04T10:00:01Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 20},
            {"timestamp": "2026-04-04T10:00:02Z", "endpoint": "/b", "severity": "INFO", "latency_ms": 30},
            {"timestamp": "2026-04-04T10:00:03Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 40},
            {"timestamp": "2026-04-04T10:00:04Z", "endpoint": "/c", "severity": "INFO", "latency_ms": 50},
        ]
        result = self.analyzer.analyze(self._payload(events, window_seconds=60, step_seconds=60, top_k=2))
        self.assertEqual(result["windows"][0]["top_endpoints"], [{"endpoint": "/a", "count": 2}, {"endpoint": "/b", "count": 2}])

    def test_tc06_single_event_percentile(self):
        events = [
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "ERROR", "latency_ms": 450},
        ]
        result = self.analyzer.analyze(self._payload(events, window_seconds=60, step_seconds=60, top_k=2))
        window = result["windows"][0]
        self.assertEqual(window["p95_latency_ms"], 450)
        self.assertEqual(window["error_rate"], 1.0)

    def test_tc07_top_k_larger_than_unique_endpoints(self):
        events = [
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 1},
            {"timestamp": "2026-04-04T10:00:01Z", "endpoint": "/b", "severity": "INFO", "latency_ms": 2},
        ]
        result = self.analyzer.analyze(self._payload(events, window_seconds=60, step_seconds=60, top_k=5))
        self.assertEqual(len(result["windows"][0]["top_endpoints"]), 2)

    def test_tc08_duplicate_timestamps_counted(self):
        events = [
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 10},
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/b", "severity": "ERROR", "latency_ms": 20},
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/b", "severity": "WARN", "latency_ms": 30},
        ]
        result = self.analyzer.analyze(self._payload(events, window_seconds=60, step_seconds=60))
        self.assertEqual(result["windows"][0]["total_events"], 3)

    def test_tc09_all_events_invalid(self):
        events = [
            {"timestamp": "bad-ts", "endpoint": "/a", "severity": "INFO", "latency_ms": 10},
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "", "severity": "INFO", "latency_ms": 10},
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "TRACE", "latency_ms": 10},
        ]
        result = self.analyzer.analyze(self._payload(events))
        self.assertEqual(result["skipped_events"], 3)
        self.assertEqual(result["windows"], [])

    def test_tc10_large_latency_values(self):
        events = [
            {"timestamp": "2026-04-04T10:00:00Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 1},
            {"timestamp": "2026-04-04T10:00:01Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 2_000_000},
            {"timestamp": "2026-04-04T10:00:02Z", "endpoint": "/a", "severity": "INFO", "latency_ms": 3},
        ]
        result = self.analyzer.analyze(self._payload(events, window_seconds=60, step_seconds=60))
        self.assertEqual(result["windows"][0]["p95_latency_ms"], 2_000_000)


if __name__ == "__main__":
    unittest.main()
