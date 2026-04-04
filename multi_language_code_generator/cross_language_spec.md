# Cross-Language Specification - Sliding Window Log Analyzer

## Algorithm Description
Analyze application logs and compute per-window reliability metrics using a fixed sliding time window.

For each window of size `window_seconds` (advanced by `step_seconds`):
- `total_events`: number of valid log events in the window
- `error_events`: number of events with severity `ERROR`
- `error_rate`: `error_events / total_events` (0 when `total_events = 0`)
- `p95_latency_ms`: 95th percentile of `latency_ms` over valid events in the window
- `top_endpoints`: top `K` endpoints by request count in the window

This specification is intended to be language-agnostic and implemented consistently in Python, JavaScript, Java, or other languages.

## Input Format
Input is a JSON object:

```json
{
  "window_seconds": 60,
  "step_seconds": 30,
  "top_k": 2,
  "events": [
    {
      "timestamp": "2026-04-04T10:00:00Z",
      "endpoint": "/api/login",
      "severity": "INFO",
      "latency_ms": 120
    }
  ]
}
```

### Field Rules
- `window_seconds`: integer, `> 0`
- `step_seconds`: integer, `> 0`
- `top_k`: integer, `>= 1`
- `events`: array of event objects
- `timestamp`: ISO-8601 UTC string
- `endpoint`: non-empty string
- `severity`: one of `INFO`, `WARN`, `ERROR`
- `latency_ms`: integer, `>= 0`

### Event Validation
- Invalid events are skipped (not counted) and should increment `skipped_events`.
- If all events are invalid, output should still be well-formed with empty windows or zeroed metrics.

## Output Format
Output is a JSON object:

```json
{
  "window_seconds": 60,
  "step_seconds": 30,
  "top_k": 2,
  "skipped_events": 1,
  "windows": [
    {
      "start": "2026-04-04T10:00:00Z",
      "end": "2026-04-04T10:01:00Z",
      "total_events": 4,
      "error_events": 1,
      "error_rate": 0.25,
      "p95_latency_ms": 310,
      "top_endpoints": [
        { "endpoint": "/api/login", "count": 2 },
        { "endpoint": "/api/search", "count": 1 }
      ]
    }
  ]
}
```

### Deterministic Rules
- Windows are ordered by ascending `start` time.
- Window interval is half-open: `[start, end)`.
- `p95_latency_ms` uses nearest-rank percentile: `rank = ceil(0.95 * n)`, 1-indexed on sorted latencies.
- Tie-break for `top_endpoints`: descending count, then ascending endpoint lexicographically.
- `error_rate` rounded to 4 decimal places.

## Edge Cases
- Empty `events` list.
- All events invalid (bad timestamp, missing endpoint, negative latency, unsupported severity).
- Multiple events with identical timestamps.
- Events exactly on window boundaries (must obey `[start, end)`).
- `top_k` greater than number of unique endpoints.
- Very large `latency_ms` values.

## Test Cases

- **TC-01 Basic mixed severities**  
  Input: 4 valid events in one 60s window, 1 with `ERROR`, latencies `[100, 120, 200, 310]`, endpoints `/a, /a, /b, /c`, `top_k=2`  
  Expected: `total_events=4`, `error_events=1`, `error_rate=0.2500`, `p95_latency_ms=310`, `top_endpoints=[(/a,2),(/b,1)]`

- **TC-02 Empty event list**  
  Input: `events=[]`, `window_seconds=60`, `step_seconds=30`  
  Expected: `skipped_events=0`, `windows=[]`

- **TC-03 Invalid records skipped**  
  Input: 5 events where 2 are invalid (negative latency, invalid severity), 3 valid with one `ERROR`  
  Expected: `skipped_events=2`, metrics computed from only 3 valid events

- **TC-04 Boundary correctness**  
  Input: events at `10:00:00Z`, `10:00:59Z`, `10:01:00Z`; window `[10:00:00,10:01:00)`  
  Expected: first two events included in first window, third excluded from first window and included in next applicable window

- **TC-05 Top-K tie break**  
  Input: endpoint counts `/b:2`, `/a:2`, `/c:1`, `top_k=2`  
  Expected: `top_endpoints=[(/a,2),(/b,2)]` (lexicographic tie-break)

- **TC-06 Single event percentile**  
  Input: one valid event with latency `450`  
  Expected: `p95_latency_ms=450`, `error_rate=1.0000` if severity is `ERROR`, otherwise `0.0000`

- **TC-07 Top-K larger than unique endpoints**  
  Input: unique endpoints = 2, `top_k=5`  
  Expected: return only 2 endpoint entries, no padding values

- **TC-08 Duplicate timestamps**  
  Input: multiple valid events with exactly the same timestamp and different endpoints  
  Expected: all events counted; no deduplication by timestamp unless explicitly required

- **TC-09 All events invalid**  
  Input: all events fail validation (bad timestamp format, empty endpoint, invalid severity)  
  Expected: `skipped_events = total_input_events`, `windows=[]` or zero-event windows according to implementation policy

- **TC-10 Large latency values**  
  Input: valid events including very large `latency_ms` values (e.g., `2000000`)  
  Expected: no overflow/format errors; percentile and counts computed correctly

## Notes for Cross-Language Consistency
- Use UTC for all parsing/formatting.
- Avoid floating-point drift in `error_rate` formatting by rounding once at output time.
- Keep sorting stable and explicit for deterministic outputs across languages.
- Ensure invalid records do not crash processing; they must be counted in `skipped_events`.
