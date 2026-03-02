// Bug 5 fixed
// Fetch user data and return the user's name in uppercase using async/await.
// To keep this testable without network access, a fetch implementation can be injected.

async function fetchUserNameUpper(userId, fetchImpl = fetch) {
  const url = `https://api.example.com/users/${userId}`;

  const response = await fetchImpl(url);
  const user = await response.json();

  return String(user.name).toUpperCase();
}

// Self-test with a fake fetch (no network)
async function main() {
  const fakeFetch = async (_url) => ({
    json: async () => ({ name: "Ada Lovelace" }),
  });

  const name = await fetchUserNameUpper(42, fakeFetch);
  console.log(name); // "ADA LOVELACE"
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
