# Bug Descriptions

## Bug 1
**File**: bug1.py  
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The function returns n+1 items instead of n when n < len(items). Should use `len(items) - n` as the start index.

## Bug 2
**File**: bug2.js  
**Intended Behavior**: Remove duplicate numbers from an array and return them in ascending order.  
**Issue Type**: Logical error (incorrect condition in implementation).  
**Notes**: The function pushes a number only when it already exists in `result`, so new unique values never get added. The condition should be inverted (add when NOT present: `!result.includes(numbers[i])`).

## Bug 3
**File**: bug3.java  
**Intended Behavior**: Calculate the average length of non-null strings in a list, ignoring nulls.  
**Issue Type**: Runtime exception (NullPointerException).  
**Notes**: No null check before calling `str.length()`. Should skip nulls to avoid exception.

## Bug 4
**File**: bug4.py  
**Intended Behavior**: Calculate the sum of all values in a dictionary where the values are numbers stored as strings.  
**Issue Type**: Data type misuse (numeric handling error).  
**Notes**: Values are numeric strings, but `total` is initialized as a string and `+=` performs concatenation (e.g. "10" + "5" -> "105"). `total` should be numeric (e.g. `0`) and each `value` should be converted (e.g. `int(value)`) before adding.

## Bug 5
**File**: bug5.js  
**Intended Behavior**: Fetch user data from an API and return the user's name in uppercase using async/await.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**: The function is not declared async but uses await. Should add `async` keyword to the function.

## Bug 6
**File**: bug6.py  
**Intended Behavior**: Find the first pair of consecutive numbers in a list that sum to a target value.  
**Issue Type**: Logic error (infinite loop).  
**Notes**: The loop never increments the index when there is no match, so `i` stays the same and the `while` condition never changes (infinite loop). Fix by incrementing `i` on every iteration (and only returning when a match is found).
