/**
 * Bug 2: Logical error with array filtering
 * This function should remove duplicate numbers from an array
 * and return them in ascending order.
 */

function removeDuplicates(numbers) {
    // Bug: Logical error - comparison should check if item is NOT in result
    let result = [];
    
    for (let i = 0; i < numbers.length; i++) {
        if (result.includes(numbers[i])) {
            result.push(numbers[i]);
        }
    }
    
    // Sort numerically
    result.sort((a, b) => a - b);
    
    return result;
}

// Test cases
console.log("Remove duplicates from [4, 2, 4, 1, 3, 2]:", 
            removeDuplicates([4, 2, 4, 1, 3, 2]));  // Expected: [1, 2, 3, 4]

console.log("Remove duplicates from [5, 5, 5, 5]:", 
            removeDuplicates([5, 5, 5, 5]));  // Expected: [5]

console.log("Remove duplicates from [1, 2, 3]:", 
            removeDuplicates([1, 2, 3]));  // Expected: [1, 2, 3]
