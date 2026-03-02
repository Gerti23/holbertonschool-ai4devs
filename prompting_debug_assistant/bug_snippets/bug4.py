"""
Bug 4: Misuse of data types
This function should calculate the sum of all values in a dictionary
where the values are numbers stored as strings.
"""

def sum_string_numbers(data):
    """
    Sums all numeric string values in a dictionary.
    
    Args:
        data: Dictionary with string values representing numbers
        
    Returns:
        Total sum of all numeric values
    """
    total = "0"  # Bug: Using string instead of int
    
    for key, value in data.items():
        if value.isdigit():
            # Bug: Concatenating strings instead of adding numbers
            total = total + value
    
    return total


# Test cases
inventory = {
    "apples": "10",
    "oranges": "25",
    "bananas": "15",
    "grapes": "30"
}

result = sum_string_numbers(inventory)
print(f"Total items: {result}")  # Expected: 80, but will get string concatenation

orders = {
    "order1": "100",
    "order2": "250",
    "order3": "75"
}

result2 = sum_string_numbers(orders)
print(f"Total orders value: {result2}")  # Expected: 425