# AI Review Log

## Inline Comments

### Security
- (line 20) `normalized()` blindly casts `line` with `int(self.line)`. If review data comes from an external source, malformed values will raise and stop the entire triage run. Consider validating fields and skipping or collecting bad records instead of failing hard. This would make the pipeline more resilient to bad payloads without hiding the problem.
- (line 24) `severity` is normalized here, but unsupported values are only rejected later in `_severity_rank()`. A clearer approach is to validate severity during normalization and return a structured error so invalid input does not surface deep inside the pipeline. Early validation also makes failures easier to trace in logs.
- (line 115) `_severity_rank()` raises `ValueError` for unknown severities. That is correct for internal invariants, but risky for untrusted review data. Consider a safe fallback or explicit exception handling in `triage_comments()` so one bad comment does not break the whole report. A per-comment error path would preserve the rest of the report.

### Performance
- (line 49-50) `_severity_rank(comment.severity)` is computed more than once per item during filtering and again later in sorting/deduplication. Caching the rank on `ReviewComment` or computing it once per loop would reduce repeated work for large review batches. The current approach is fine for small inputs, but it will scale less well as review volume grows.
- (line 57-64) The sort key recomputes `_severity_rank(item.severity)` for every item. Since severity is already known when triaging, storing the numeric rank alongside `TriageItem` would make sorting cheaper and simpler. It would also remove repeated string normalization during sort comparisons.
- (line 98-101) `_path_allowed()` uses `fnmatch()` over every include/exclude pattern for each comment. If the dataset grows, consider precompiling or normalizing patterns once in `TriageConfig` to avoid repeated wildcard matching overhead. That would help especially when the same config is reused across many review items.

### Maintainability
- (line 74-78) The scoring formula uses several magic numbers (`10`, `8.0`, `6.0`, `4.0`, `2.0`, `1.5`). These should be extracted into named constants or a small scoring strategy object so future changes are easier to reason about. That would also make it simpler to tune severity weights without editing arithmetic in multiple places.
- (line 89-95) Deduplication keying uses `(file_path, line, message.lower())`, which is a little brittle because it depends on exact message text. Consider documenting the dedupe policy or factoring it into a helper so the behavior is easier to change and test. A helper would also make it clearer whether semantic duplicates or exact duplicates are intended.
- (line 66) `max(1, config.top_k)` silently converts `top_k=0` into `1`, which may surprise callers. It would be clearer to validate `top_k` in `TriageConfig` and either allow zero explicitly or raise a descriptive error. Surprising implicit coercions tend to cause bugs in calling code later.
- (line 103-107) `_count_by_file()` sorts counts before returning, but that ordering rule is not documented. A short docstring or a named helper would make the report semantics easier for future contributors to understand. This is especially useful because report ordering often becomes part of the public contract.

## Global Feedback
- The feature is solid and test coverage is good, but the API would benefit from explicit input validation and docstrings for the main public types (`ReviewComment`, `TriageConfig`, `triage_comments()`). Clearer API contracts would make the module easier to reuse and safer for external inputs.
- Consider adding tests for invalid severities, malformed `line` values, and `top_k=0` to lock down edge-case behavior and prevent regressions. These edge cases are where triage systems often fail in practice, so covering them will make the feature more robust.
- If this module is intended for larger review volumes, a future iteration could return severity ranks directly in `TriageItem` to avoid repeated ranking work during sort and reporting. That change would improve performance and also simplify the comparator logic.
