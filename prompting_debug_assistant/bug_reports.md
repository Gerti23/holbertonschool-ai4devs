## Bug Report – [bug1.py](prompting_debug_assistant/bug_snippets/bug1.py)
- **Summary**: Off-by-one error in list slicing returns one extra element.
- **Root Cause**: Start index computed as `len(items) - n - 1`, shifting the slice one position too far left.
- **Resolution**: AI suggested using `len(items) - n` or `items[-n:]`. Manual choice in [bug1_fixed.py](prompting_debug_assistant/bug_fixes/bug1_fixed.py) used `items[-n:]` with guards for `n <= 0` and `n >= len(items)`.
- **Lesson Learned**: Always test slice boundaries and edge cases like `n == 0` and `n == len(items)`.

## Bug Report – [bug2.js](prompting_debug_assistant/bug_snippets/bug2.js)
- **Summary**: Deduplication logic is reversed, preventing unique values from being collected.
- **Root Cause**: The implementation pushes an element only when it already exists in the result array (`result.includes(...)`), instead of when it does not.
- **Resolution**: AI suggested inverting the condition (`!result.includes(...)`) and also suggested a `Set` approach. Manual choice in [bug2_fixed.js](prompting_debug_assistant/bug_fixes/bug2_fixed.js) used `new Set(...)` for simpler and more reliable deduplication, then sorted numerically.
- **Lesson Learned**: When implementing “add if missing” logic, verify the condition with a small input and prefer standard library data structures (like `Set`) when appropriate.

## Bug Report – [bug3.java](prompting_debug_assistant/bug_snippets/bug3.java)
- **Summary**: Runtime exception occurs when encountering `null` strings while computing average length.
- **Root Cause**: Code calls `str.length()` without checking for `null`, causing a `NullPointerException`. It also counts null entries, which contradicts “ignore nulls”.
- **Resolution**: AI suggested skipping nulls before calling `length()` and incrementing `count` only for non-null values. Manual fix in [bug3_fixed.java](prompting_debug_assistant/bug_fixes/bug3_fixed.java) added `if (str == null) continue;` and updated counting accordingly.
- **Lesson Learned**: For collections that may contain nulls, enforce null-handling rules explicitly in the loop (or use APIs that model missing values clearly).

## Bug Report – [bug4.py](prompting_debug_assistant/bug_snippets/bug4.py)
- **Summary**: Summation performs string concatenation instead of numeric addition.
- **Root Cause**: `total` is initialized as a string and `+=` concatenates values (e.g. "10" + "5" → "105"), returning the wrong type and value.
- **Resolution**: AI suggested initializing `total = 0` and converting each `value` with `int(value)`. Manual fix in [bug4_fixed.py](prompting_debug_assistant/bug_fixes/bug4_fixed.py) implemented integer accumulation.
- **Lesson Learned**: Initialize accumulators with the correct type and validate assumptions when inputs are strings representing numbers.

## Bug Report – [bug5.js](prompting_debug_assistant/bug_snippets/bug5.js)
- **Summary**: JavaScript syntax error due to `await` usage in a non-async function.
- **Root Cause**: `await` is only valid inside an `async` function (or certain top-level module contexts). Using it in a normal function makes the file fail to parse.
- **Resolution**: AI suggested adding `async` and returning/awaiting the Promise correctly, with an alternative Promise-chain fix. Manual fix in [bug5_fixed.js](prompting_debug_assistant/bug_fixes/bug5_fixed.js) declared the function `async` and also added optional `fetch` injection plus a mocked self-test to validate behavior without network dependency.
- **Lesson Learned**: Treat async as part of the function’s contract: if callers need a value from async work, return a Promise and design code to be testable (dependency injection/mocking).

## Bug Report – [bug6.py](prompting_debug_assistant/bug_snippets/bug6.py)
- **Summary**: Loop can become infinite when no matching consecutive pair is found at the current index.
- **Root Cause**: Index `i` is not incremented in the non-match path, so the loop condition never progresses.
- **Resolution**: AI suggested incrementing `i` every iteration or switching to a `for` loop. Manual fix in [bug6_fixed.py](prompting_debug_assistant/bug_fixes/bug6_fixed.py) used a `for` loop over indices for clarity and safety.
- **Lesson Learned**: In iterative search loops, ensure progress is made on every path (match and non-match) to avoid infinite loops.
