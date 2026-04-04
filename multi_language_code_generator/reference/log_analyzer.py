from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from math import ceil
from typing import Any, Dict, List, Optional, Tuple


VALID_SEVERITIES = {"INFO", "WARN", "ERROR"}


@dataclass(frozen=True)
class LogEvent:
    timestamp: datetime
    endpoint: str
    severity: str
    latency_ms: int


def _parse_utc_timestamp(value: Any) -> Optional[datetime]:
    if not isinstance(value, str) or not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def _format_utc_timestamp(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _validate_event(raw: Any) -> Optional[LogEvent]:
    if not isinstance(raw, dict):
        return None

    timestamp = _parse_utc_timestamp(raw.get("timestamp"))
    endpoint = raw.get("endpoint")
    severity = raw.get("severity")
    latency_ms = raw.get("latency_ms")

    if timestamp is None:
        return None
    if not isinstance(endpoint, str) or not endpoint.strip():
        return None
    if severity not in VALID_SEVERITIES:
        return None
    if not isinstance(latency_ms, int) or latency_ms < 0:
        return None

    return LogEvent(
        timestamp=timestamp,
        endpoint=endpoint,
        severity=severity,
        latency_ms=latency_ms,
    )


def _nearest_rank_p95(latencies: List[int]) -> int:
    sorted_latencies = sorted(latencies)
    rank = ceil(0.95 * len(sorted_latencies))
    return sorted_latencies[rank - 1]


class SlidingWindowLogAnalyzer:
    def validate_payload(self, payload: Dict[str, Any]) -> Tuple[int, int, int, List[Any]]:
        window_seconds = payload.get("window_seconds")
        step_seconds = payload.get("step_seconds")
        top_k = payload.get("top_k")
        raw_events = payload.get("events", [])

        if not isinstance(window_seconds, int) or window_seconds <= 0:
            raise ValueError("window_seconds must be an integer > 0")
        if not isinstance(step_seconds, int) or step_seconds <= 0:
            raise ValueError("step_seconds must be an integer > 0")
        if not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be an integer >= 1")
        if not isinstance(raw_events, list):
            raise ValueError("events must be a list")

        return window_seconds, step_seconds, top_k, raw_events

    def parse_event(self, raw_event: Any) -> Optional[LogEvent]:
        return _validate_event(raw_event)

    def parse_events(self, raw_events: List[Any]) -> Tuple[List[LogEvent], int]:
        valid_events: List[LogEvent] = []
        skipped_events = 0

        for item in raw_events:
            event = self.parse_event(item)
            if event is None:
                skipped_events += 1
                continue
            valid_events.append(event)

        valid_events.sort(key=lambda event: event.timestamp)
        return valid_events, skipped_events

    def compute_window_metrics(self, events_in_window: List[LogEvent], top_k: int) -> Dict[str, Any]:
        total_events = len(events_in_window)
        error_events = sum(1 for event in events_in_window if event.severity == "ERROR")
        error_rate = round((error_events / total_events), 4) if total_events else 0.0
        latencies = [event.latency_ms for event in events_in_window]
        p95_latency_ms = _nearest_rank_p95(latencies) if latencies else 0

        endpoint_counts = Counter(event.endpoint for event in events_in_window)
        ranked_endpoints = sorted(endpoint_counts.items(), key=lambda pair: (-pair[1], pair[0]))
        top_endpoints = [
            {"endpoint": endpoint, "count": count}
            for endpoint, count in ranked_endpoints[:top_k]
        ]

        return {
            "total_events": total_events,
            "error_events": error_events,
            "error_rate": error_rate,
            "p95_latency_ms": p95_latency_ms,
            "top_endpoints": top_endpoints,
        }

    def generate_windows(
        self,
        valid_events: List[LogEvent],
        window_seconds: int,
        step_seconds: int,
        top_k: int,
    ) -> List[Dict[str, Any]]:
        if not valid_events:
            return []

        window_size = timedelta(seconds=window_seconds)
        step_size = timedelta(seconds=step_seconds)

        min_ts = valid_events[0].timestamp
        max_ts = valid_events[-1].timestamp

        windows: List[Dict[str, Any]] = []
        start = min_ts

        while start <= max_ts:
            end = start + window_size
            in_window = [event for event in valid_events if start <= event.timestamp < end]
            metrics = self.compute_window_metrics(in_window, top_k)
            windows.append(
                {
                    "start": _format_utc_timestamp(start),
                    "end": _format_utc_timestamp(end),
                    **metrics,
                }
            )
            start += step_size

        return windows

    def analyze(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        window_seconds, step_seconds, top_k, raw_events = self.validate_payload(payload)
        valid_events, skipped_events = self.parse_events(raw_events)

        if not valid_events:
            return {
                "window_seconds": window_seconds,
                "step_seconds": step_seconds,
                "top_k": top_k,
                "skipped_events": skipped_events,
                "windows": [],
            }

        windows = self.generate_windows(valid_events, window_seconds, step_seconds, top_k)

        return {
            "window_seconds": window_seconds,
            "step_seconds": step_seconds,
            "top_k": top_k,
            "skipped_events": skipped_events,
            "windows": windows,
        }
