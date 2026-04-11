# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return exactly the last `n` items from a list while handling `n = 0` and non-negative values.
- **Current Issue**: Off-by-one slicing (`len(items) - n - 1`) returns one extra element when enough items exist.

## bug2.js
- **Intended Behavior**: Merge user settings into defaults, including intentional falsy values like `0` or `false`.
- **Current Issue**: Conditional check `if (userSettings[key])` skips valid falsy overrides.

## bug3.java
- **Intended Behavior**: Return the first non-repeating character, and signal "not found" when no unique character exists.
- **Current Issue**: Returns `text.charAt(0)` even when every character repeats, producing an incorrect result.

## bug4.go
- **Intended Behavior**: Compute success percentage with decimal precision: `((total - failed) / total) * 100`.
- **Current Issue**: Performs integer division before converting to float, causing truncated percentages.

## bug5.py
- **Intended Behavior**: Normalize tags and remove duplicates while preserving original encounter order.
- **Current Issue**: Converts to `set` and back to `list`, which removes deterministic order.
