"""Bug 1 fixed

Return the last n items of a list.
"""

from typing import List, TypeVar

T = TypeVar("T")


def last_n(items: List[T], n: int) -> List[T]:
    if n <= 0:
        return []
    if n >= len(items):
        return list(items)
    return items[-n:]


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(last_n(data, 2))
