/**
 * Async Data Fetcher Demo
 */

const { fetchWithRetry } = require('./fetcher');

async function main() {
    console.log("Async Data Fetcher Demo\n");

    // Scenario 1: Successful Fetch
    console.log("1. Fetching valid data...");
    try {
        const data = await fetchWithRetry('https://jsonplaceholder.typicode.com/todos/1');
        console.log("Success:", data);
    } catch (error) {
        console.error("Failed:", error.message);
    }

    console.log("\n" + "-".repeat(50) + "\n");

    // Scenario 2: Failed Fetch (Simulated with invalid URL)
    console.log("2. Fetching invalid URL (will retry)...");
    try {
        await fetchWithRetry('https://jsonplaceholder.typicode.com/invalid-endpoint', 2, 500);
    } catch (error) {
        console.log("Expected Failure Caught:", error.message);
    }
}

if (require.main === module) {
    main();
}
