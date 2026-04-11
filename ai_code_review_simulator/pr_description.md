# Pull Request: Add AI Review Comment Triage Engine

## Summary
Implements a new triage feature that prioritizes code review comments by severity and category, removes duplicates, supports path include/exclude filters, and returns ranked actionable items with summary metrics.

## Changes
- Added triage feature in `review_engine.py` (~150 LOC):
  - `ReviewComment`, `TriageConfig`, `TriageItem`, and `TriageReport` data models
  - `triage_comments()` pipeline with:
    - severity threshold filtering
    - path include/exclude filtering via glob patterns
    - deduplication by `(file_path, line, message)` keeping highest severity
    - score-based prioritization and `top_k` limiting
    - aggregated counts by file and by severity
- Added unit tests in `tests/test_review_engine.py`:
  - minimum severity filtering
  - include/exclude path filtering
  - deduplication correctness
  - top-k limiting
  - report aggregation counts
- Added usage note in `README.md` with test command.

## Context
- **Motivation**: Code review pipelines produce noisy, duplicated feedback. This feature simulates AI-assisted prioritization so reviewers can address highest-impact findings first.
- **Related Issue**: N/A (feature-driven sprint task)
- **Scope**: Small, meaningful feature with focused logic and tests.

## Validation
- Test command: `python3 -m unittest discover -s tests -p "test_*.py"`
- Result: **All tests passed (5/5)**
