import unittest

from multi_language_code_generator.reference.log_analyzer import SlidingWindowLogAnalyzer


class TestTC14NonListEvents(unittest.TestCase):
    def test_non_list_events_raises(self):
        analyzer = SlidingWindowLogAnalyzer()
        with self.assertRaises(ValueError):
            analyzer.analyze({"window_seconds": 60, "step_seconds": 30, "top_k": 2, "events": {}})


if __name__ == "__main__":
    unittest.main()
