"""
## Bug 1 – bug1.py
**Intended Behavior**: Return exactly the last n items of a list (e.g., get_last_n_items([1,2,3,4,5], 2) → [4, 5]).  
**Issue Type**: Off-by-one error.  
**Notes**: The function incorrectly returns n+1 items when n < len(items) due to the wrong start index (`len(items) - n - 1`). Should use `len(items) - n` as the start index to return the correct number of items.
"""
def get_last_n_items(items, n):
    """
    Returns the last n items from a list.
    
    Args:
        items: List of items
        n: Number of items to return from the end
        
    Returns:
        List containing the last n items
    """
    if n == 0:
        return []
    
    if n >= len(items):
        return items
    
    # Bug: Off-by-one error in the slicing
        start_index = len(items) - n
    return items[start_index:]


# Test cases
test_list = [1, 2, 3, 4, 5]
print("Last 2 items:", get_last_n_items(test_list, 2))  # Expected: [4, 5]
print("Last 5 items:", get_last_n_items(test_list, 5))  # Expected: [1, 2, 3, 4, 5]
print("Last 1 item:", get_last_n_items(test_list, 1))   # Expected: [5]