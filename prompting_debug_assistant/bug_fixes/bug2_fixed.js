// Bug 2 fixed
// Remove duplicates from an array of numbers and return ascending order.

function dedupeAndSort(numbers) {
  return [...new Set(numbers)].sort((a, b) => a - b);
}

// Simple test
const input = [3, 1, 2, 3, 2, 4, 1];
console.log(dedupeAndSort(input)); // [1,2,3,4]
