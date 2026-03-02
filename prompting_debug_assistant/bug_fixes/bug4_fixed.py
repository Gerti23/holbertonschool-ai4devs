"""Bug 4 fixed

Sum values in a dict where values are numeric strings.
"""

from typing import Dict


def sum_string_values(values: Dict[str, str]) -> int:
    total = 0
    for value in values.values():
        total += int(value)
    return total


if __name__ == "__main__":
    d = {"apples": "10", "oranges": "5", "pears": "2"}
    print(sum_string_values(d))
