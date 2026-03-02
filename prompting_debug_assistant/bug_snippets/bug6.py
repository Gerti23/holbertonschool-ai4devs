"""
## Bug 6 – bug6.py
**Intended Behavior**: Find and return the first pair of consecutive numbers in a list that sum to a target value, or None if not found.  
**Issue Type**: Logic error (infinite loop).  
**Notes**: The index is only incremented when a match is found, causing an infinite loop if no match exists. Should increment the index on every iteration.
"""

def find_consecutive_pair(numbers, target):
    """
    Finds the first pair of consecutive numbers that sum to target.
    
    Args:
        numbers: List of integers
        target: Target sum to find
        
    Returns:
        Tuple of (index, value1, value2) or None if not found
    """
    i = 0 
    # Bug: Loop condition and increment logic can cause infinite loop
    while i < len(numbers):
        if i + 1 < len(numbers):
            current_sum = numbers[i] + numbers[i + 1]
            
            if current_sum == target:
                return (i, numbers[i], numbers[i + 1])
            
            # Bug: Only increments when sum matches; 
            # if no match is found, infinite loop occurs
            if current_sum != target:
                continue  # Goes back to while without incrementing i
        else:
            i = 0
            while i < len(numbers) - 1:
                if numbers[i] + numbers[i+1] == target:
                    return (numbers[i], numbers[i+1])
                i += 1  # Fixed: Always increment i
print("Find pair summing to 20:", find_consecutive_pair(test_numbers, 20))