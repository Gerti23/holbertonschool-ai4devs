# Bug Descriptions

---

## Bug 1

- **File:** `bug1.py`
- **Function:** `get_last_n_items(items, n)`

### Intended Behavior
Return the last `n` elements of a list. Example: `get_last_n_items([1, 2, 3, 4, 5], 2)` → `[4, 5]`.

### Issue Type
Off-by-one error.

### Bug Description
The start index is calculated as `len(items) - n - 1` instead of `len(items) - n`. The extra `- 1` shifts the slice one position too far left, including one more element than requested.

### Impact
The function silently returns `n + 1` items instead of `n`. No exception is raised. Example: `get_last_n_items([1, 2, 3, 4, 5], 2)` returns `[3, 4, 5]` instead of `[4, 5]`.

### Fix
Change `start_index = len(items) - n - 1` to `start_index = len(items) - n`.

---

## Bug 2

- **File:** `bug2.js`
- **Function:** `removeDuplicates(numbers)`

### Intended Behavior
Remove duplicate numbers from an array and return the unique values sorted in ascending order. Example: `removeDuplicates([4, 2, 4, 1, 3, 2])` → `[1, 2, 3, 4]`.

### Issue Type
Logical error.

### Bug Description
The condition `if (result.includes(numbers[i]))` adds a number only when it is already in the result, which is the inverse of what is needed. It should be `if (!result.includes(numbers[i]))` to add numbers not yet seen.

### Impact
The function returns an empty array for inputs with all unique values, and incorrectly handles duplicates for all other inputs. The sorted output is therefore also wrong.

### Fix
Change `if (result.includes(numbers[i]))` to `if (!result.includes(numbers[i]))`.

---

## Bug 3

- **File:** `bug3.java`
- **Method:** `calculateAverageLength(List<String> strings)`

### Intended Behavior
Calculate the average character length of all non-null strings in a list, ignoring `null` entries. Example: `["hello", "world", null, "test"]` → average of lengths of the three non-null strings.

### Issue Type
Runtime exception — NullPointerException.

### Bug Description
Inside the for-each loop, `str.length()` is called without a prior null check. When a `null` element is reached, the JVM throws a `NullPointerException` and the program terminates immediately.

### Impact
The program crashes at runtime on any list that contains a `null` value. No result is computed or returned.

### Fix
Add `if (str == null) continue;` at the start of the loop body before calling `str.length()`.

---

## Bug 4

- **File:** `bug4.py`
- **Function:** `sum_string_numbers(data)`

### Intended Behavior
Parse numeric strings stored as dictionary values and return their integer sum. Example: `{"apples": "10", "oranges": "25", "bananas": "15", "grapes": "30"}` → `80`.

### Issue Type
Data type misuse.

### Bug Description
The accumulator `total` is initialized as the string `"0"` instead of the integer `0`. The loop then performs `total = total + value`, which concatenates strings instead of adding integers.

### Impact
The function returns a concatenated string (e.g., `"010251530"`) instead of the expected integer (`80`). No exception is raised, making the bug completely silent.

### Fix
Initialize `total = 0` (integer) and convert each value before adding: `total = total + int(value)`.

---

## Bug 5

- **File:** `bug5.js`
- **Function:** `getUserName(userId)`

### Intended Behavior
Call a simulated asynchronous API to fetch user data by ID and return the user's name in uppercase, using `async/await` for asynchronous control flow.

### Issue Type
Syntax error.

### Bug Description
The function containing `await fetchUserData(userId)` is not declared with the `async` keyword. In JavaScript, `await` is only valid inside an `async` function; using it elsewhere causes a `SyntaxError`.

### Impact
The script fails at parse time and no code is executed. No user data is fetched and no name is returned.

### Fix
Add the `async` keyword to the function declaration: `async function getUserName(userId)`.

---

## Bug 6

- **File:** `bug6.py`
- **Function:** `find_consecutive_pair(numbers, target)`

### Intended Behavior
Iterate through a list and return the first pair of consecutive elements whose sum equals the given target. Return `None` if no such pair exists.

### Issue Type
Logic error — infinite loop.

### Bug Description
The loop index `i` is incremented only inside the `if` block that checks for a matching pair. When the current pair does not match, `i` is never incremented, causing the same pair to be evaluated forever.

### Impact
If the first pair checked does not match the target, the function hangs indefinitely in an infinite loop and never returns.

### Fix
Move `i += 1` outside the `if` block so it executes on every iteration, or replace the `while` loop with `for i in range(len(numbers) - 1)`.
