/**
 ## Bug 5 – bug5.js
**Intended Behavior**: Fetch user data from an API and return the user's name in uppercase using async/await.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**: The function uses `await` but is not declared as `async`. Should add the `async` keyword to the function declaration.
 */

// Simulated API call
function fetchUserData(userId) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ id: userId, name: "John Doe", email: "john@example.com" });
        }, 1000);
    });
}

// Bug: Missing async keyword but using await
async function getUserName(userId) {
    try {
        // Bug: await used in non-async function
        const userData = await fetchUserData(userId);
        return userData.name.toUpperCase();
    } catch (error) {
        console.error("Error fetching user data:", error);
        return null;
    }
}

// Test case
console.log("Fetching user name...");
getUserName(123).then(name => {
    console.log("User name:", name);  // Expected: "JOHN DOE"
}).catch(error => {
    console.error("Failed:", error);
});