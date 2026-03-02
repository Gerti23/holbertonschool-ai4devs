"""
## Bug 4 – bug4.py
**Intended Behavior**: Calculate the sum of all dictionary values, where values are numeric strings (e.g., {"apples": "10", ...} → 80).  
**Issue Type**: Data type misuse.  
**Notes**: The total is initialized as a string and concatenates values instead of adding them as integers. Should use integer addition (`total = 0; total += int(value)`).
"""

def sum_string_numbers(data):
    total = 0  # Fixed: Use integer for total
    for key, value in data.items():
        if value.isdigit():
            total += int(value)
    return total
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