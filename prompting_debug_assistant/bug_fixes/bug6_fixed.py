"""Bug 6 fixed

Find the first pair of consecutive numbers that sum to target.
"""

from typing import List, Optional, Tuple


def first_consecutive_pair(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    for i in range(len(nums) - 1):
        if nums[i] + nums[i + 1] == target:
            return (nums[i], nums[i + 1])
    return None


if __name__ == "__main__":
    print(first_consecutive_pair([1, 2, 4, 3], 7))
