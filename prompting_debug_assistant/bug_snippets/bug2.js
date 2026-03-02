/**
 * ## Bug 2 – bug2.js
 * Logic error in duplicate removal and sorting
 * This function should remove duplicates from an array of numbers and return a sorted array of unique values. 
 * The original code had a logic error where it added duplicates to the result array and then sorted it as strings, leading to incorrect results.
 */

function removeDuplicates(numbers) {
    // Fixed: Only add if not already present
    let result = [];
    for (let i = 0; i < numbers.length; i++) {
        if (!result.includes(numbers[i])) {
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