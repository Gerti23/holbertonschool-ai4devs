from typing import List


def last_n_items(items: List[int], n: int) -> List[int]:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return []

    start = len(items) - n
    if start < 0:
        start = 0
    return items[start:]


if __name__ == "__main__":
    print(last_n_items([10, 20, 30, 40, 50], 2))
