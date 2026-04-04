import unittest

from multi_language_code_generator.reference.log_analyzer import SlidingWindowLogAnalyzer


class TestTC13BadParams(unittest.TestCase):
    def test_invalid_window_seconds_raises(self):
        analyzer = SlidingWindowLogAnalyzer()
        with self.assertRaises(ValueError):
            analyzer.analyze({"window_seconds": 0, "step_seconds": 30, "top_k": 2, "events": []})


if __name__ == "__main__":
    unittest.main()
