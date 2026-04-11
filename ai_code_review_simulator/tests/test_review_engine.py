import unittest

from review_engine import ReviewComment, TriageConfig, triage_comments


class TestReviewEngine(unittest.TestCase):
    def test_filters_by_min_severity(self):
        comments = [
            ReviewComment("src/a.py", 10, "ana", "low", "nit: rename variable"),
            ReviewComment("src/a.py", 12, "ana", "high", "possible crash", "correctness"),
        ]

        report = triage_comments(comments, TriageConfig(min_severity="medium"))

        self.assertEqual(len(report.items), 1)
        self.assertEqual(report.items[0].severity, "high")

    def test_path_include_exclude(self):
        comments = [
            ReviewComment("src/api/users.py", 20, "tom", "high", "auth issue", "security"),
            ReviewComment("tests/test_users.py", 8, "tom", "high", "bad test", "maintainability"),
            ReviewComment("src/generated/client.py", 5, "tom", "critical", "unsafe eval", "security"),
        ]

        config = TriageConfig(
            min_severity="low",
            include_paths=("src/**/*.py",),
            exclude_paths=("src/generated/*",),
        )
        report = triage_comments(comments, config)

        self.assertEqual([item.file_path for item in report.items], ["src/api/users.py"])

    def test_dedup_keeps_highest_severity(self):
        comments = [
            ReviewComment("src/a.py", 7, "ana", "medium", "null check missing"),
            ReviewComment("src/a.py", 7, "bob", "critical", "null check missing", "correctness"),
        ]

        report = triage_comments(comments, TriageConfig())

        self.assertEqual(len(report.items), 1)
        self.assertEqual(report.items[0].severity, "critical")

    def test_top_k_limits_items(self):
        comments = [
            ReviewComment("src/a.py", 1, "ana", "critical", "sql injection", "security"),
            ReviewComment("src/b.py", 1, "ana", "high", "n+1 query", "performance"),
            ReviewComment("src/c.py", 1, "ana", "medium", "complex function", "maintainability"),
        ]

        report = triage_comments(comments, TriageConfig(top_k=2))

        self.assertEqual(len(report.items), 2)
        self.assertTrue(report.items[0].score >= report.items[1].score)

    def test_aggregates_counts(self):
        comments = [
            ReviewComment("src/a.py", 3, "ana", "high", "bug one", "correctness"),
            ReviewComment("src/a.py", 5, "ana", "high", "bug two", "correctness"),
            ReviewComment("src/b.py", 2, "ana", "medium", "slow loop", "performance"),
        ]

        report = triage_comments(comments, TriageConfig())

        self.assertEqual(report.by_file_counts, {"src/a.py": 2, "src/b.py": 1})
        self.assertEqual(report.by_severity_counts, {"high": 2, "medium": 1})


if __name__ == "__main__":
    unittest.main()
