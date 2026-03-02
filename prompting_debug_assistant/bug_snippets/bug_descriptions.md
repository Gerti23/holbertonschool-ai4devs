
# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The function returns n+1 items instead of n when n < len(items). Should use `len(items) - n` as the start index.

## Bug 2 – bug2.js
**Intended Behavior**: Remove duplicate numbers from an array and return them in ascending order.  
**Issue Type**: Logical error.  
**Notes**: The function adds numbers to the result only if already present. Should add if not present (`!result.includes(numbers[i])`).

## Bug 3 – bug3.java
**Intended Behavior**: Calculate the average length of non-null strings in a list, ignoring nulls.  
**Issue Type**: Runtime exception (NullPointerException).  
**Notes**: No null check before calling `str.length()`. Should skip nulls to avoid exception.

## Bug 4 – bug4.py
**Intended Behavior**: Calculate the sum of all values in a dictionary where the values are numbers stored as strings.  
**Issue Type**: Data type misuse.  
**Notes**: The total is a string and concatenates values. Should use integer addition (`total = 0; total += int(value)`).

## Bug 5 – bug5.js
**Intended Behavior**: Fetch user data from an API and return the user's name in uppercase using async/await.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**: The function is not declared async but uses await. Should add `async` keyword to the function.

## Bug 6 – bug6.py
**Intended Behavior**: Find the first pair of consecutive numbers in a list that sum to a target value.  
**Issue Type**: Logic error (infinite loop).  
**Notes**: The index is only incremented on match, causing infinite loop if no match. Should increment index every iteration.
