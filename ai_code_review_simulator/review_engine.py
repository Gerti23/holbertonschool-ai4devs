from __future__ import annotations

from dataclasses import dataclass
from fnmatch import fnmatch
from typing import Iterable

SEVERITY_RANK = {"low": 1, "medium": 2, "high": 3, "critical": 4}


@dataclass(frozen=True)
class ReviewComment:
    file_path: str
    line: int
    author: str
    severity: str
    message: str
    category: str = "general"

    def normalized(self) -> "ReviewComment":
        return ReviewComment(
            file_path=self.file_path.strip(),
            line=max(1, int(self.line)),
            author=self.author.strip() or "anonymous",
            severity=self.severity.strip().lower(),
            message=" ".join(self.message.split()),
            category=self.category.strip().lower() or "general",
        )


@dataclass(frozen=True)
class TriageConfig:
    min_severity: str = "low"
    include_paths: tuple[str, ...] = ()
    exclude_paths: tuple[str, ...] = ()
    top_k: int = 10


@dataclass(frozen=True)
class TriageItem:
    file_path: str
    line: int
    severity: str
    score: float
    message: str
    author: str
    category: str


@dataclass(frozen=True)
class TriageReport:
    items: list[TriageItem]
    by_file_counts: dict[str, int]
    by_severity_counts: dict[str, int]


def triage_comments(comments: Iterable[ReviewComment], config: TriageConfig) -> TriageReport:
    min_rank = _severity_rank(config.min_severity)

    candidates: list[ReviewComment] = []
    for raw_comment in comments:
        comment = raw_comment.normalized()
        if _severity_rank(comment.severity) < min_rank:
            continue
        if not _path_allowed(comment.file_path, config.include_paths, config.exclude_paths):
            continue
        candidates.append(comment)

    deduped = _deduplicate(candidates)

    triage_items = [_to_triage_item(comment) for comment in deduped]
    triage_items.sort(
        key=lambda item: (
            -item.score,
            -_severity_rank(item.severity),
            item.file_path,
            item.line,
        )
    )

    limited_items = triage_items[: max(1, config.top_k)]
    return TriageReport(
        items=limited_items,
        by_file_counts=_count_by_file(limited_items),
        by_severity_counts=_count_by_severity(limited_items),
    )


def _to_triage_item(comment: ReviewComment) -> TriageItem:
    base = float(_severity_rank(comment.severity) * 10)
    category_bonus = {
        "security": 8.0,
        "correctness": 6.0,
        "performance": 4.0,
        "maintainability": 2.0,
        "general": 1.0,
    }.get(comment.category, 1.0)

    message_penalty = min(len(comment.message) / 200.0, 1.5)
    score = round(base + category_bonus - message_penalty, 2)

    return TriageItem(
        file_path=comment.file_path,
        line=comment.line,
        severity=comment.severity,
        score=score,
        message=comment.message,
        author=comment.author,
        category=comment.category,
    )


def _deduplicate(comments: Iterable[ReviewComment]) -> list[ReviewComment]:
    best_by_key: dict[tuple[str, int, str], ReviewComment] = {}
    for comment in comments:
        key = (comment.file_path, comment.line, comment.message.lower())
        current = best_by_key.get(key)
        if current is None or _severity_rank(comment.severity) > _severity_rank(current.severity):
            best_by_key[key] = comment
    return list(best_by_key.values())


def _path_allowed(path: str, includes: tuple[str, ...], excludes: tuple[str, ...]) -> bool:
    if includes and not any(fnmatch(path, pattern) for pattern in includes):
        return False
    if excludes and any(fnmatch(path, pattern) for pattern in excludes):
        return False
    return True


def _count_by_file(items: list[TriageItem]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in items:
        counts[item.file_path] = counts.get(item.file_path, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))


def _count_by_severity(items: list[TriageItem]) -> dict[str, int]:
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for item in items:
        counts[item.severity] = counts.get(item.severity, 0) + 1
    return {key: value for key, value in counts.items() if value > 0}


def _severity_rank(severity: str) -> int:
    normalized = severity.strip().lower()
    if normalized not in SEVERITY_RANK:
        raise ValueError(f"Unsupported severity: {severity}")
    return SEVERITY_RANK[normalized]
