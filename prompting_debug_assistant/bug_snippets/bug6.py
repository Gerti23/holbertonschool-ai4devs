"""
Bug 6: Loop logic issue with infinite loop potential
This function should find the first pair of consecutive numbers 
in a list that sum to a target value.
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
            i += 1
    
    return None


# Test cases
test_numbers = [1, 3, 5, 7, 9, 11]
print("Find pair summing to 12:", find_consecutive_pair(test_numbers, 12))
# Expected: (2, 5, 7)

print("Find pair summing to 20:", find_consecutive_pair(test_numbers, 20))
# Expected: (4, 9, 11)