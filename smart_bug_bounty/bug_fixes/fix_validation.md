# Fix Validation

## bug1.py
- **Original Issue**: Off-by-one slice returned `n + 1` items in many cases.
- **Fix Applied**: Changed start index from `len(items) - n - 1` to `len(items) - n` and kept lower-bound guard.
- **Test Results**: Automated Python tests passed (`3/3`).
  - `[10,20,30,40,50], n=2` → `[40,50]`
  - `[1,2], n=5` → `[1,2]`
  - `[1,2,3], n=0` → `[]`

## bug2.js
- **Original Issue**: Truthy check skipped valid falsy overrides (`0`, `false`, `""`).
- **Fix Applied**: Replaced truthy condition with own-property check and direct assignment.
- **Test Results**: Automated JavaScript tests passed (`3/3`) using a user-space Node runtime.
  - `{ retries: 3, verbose: true } + { retries: 0 }` → `{ retries: 0, verbose: true }`
  - `{ enabled: true, timeout: 10 } + { enabled: false }` → `{ enabled: false, timeout: 10 }`
  - `{ timeoutMs: 5000 } + { timeoutMs: 0 }` → `{ timeoutMs: 0 }`

## bug3.java
- **Original Issue**: Returned first character when no unique char existed; unsafe for empty input.
- **Fix Applied**: Added empty/null guard and return sentinel `'\0'` when no unique character is found.
- **Test Results**: Automated Java tests passed (`3/3`) using a user-space JDK.
  - `firstUniqueChar("swiss")` → `'w'`
  - `firstUniqueChar("aabbcc")` → `'\0'`
  - `firstUniqueChar("")` → `'\0'`

## bug4.go
- **Original Issue**: Integer division truncated success ratio before float conversion.
- **Fix Applied**: Cast operands to `float64` before division.
- **Test Results**: Automated Go unit test passed (`3/3`) using a user-space Go runtime.
  - `successRate(9, 2)` ≈ `77.7778`
  - `successRate(10, 0)` = `100.0`
  - `successRate(0, 0)` = `0.0`

## bug5.py
- **Original Issue**: `set`-based dedupe lost input order.
- **Fix Applied**: Replaced with `list(dict.fromkeys(cleaned))` to preserve insertion order.
- **Test Results**: Automated Python tests passed (`3/3`).
  - `"Python, api, python, backend, Api"` → `["python", "api", "backend"]`
  - `" one , two , one "` → `["one", "two"]`
  - `" , ,A,,a, "` → `["a"]`
