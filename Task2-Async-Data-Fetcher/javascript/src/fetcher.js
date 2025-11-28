/**
 * Async Data Fetcher Module
 */

/**
 * Fetches data from a URL with retry logic.
 * 
 * @param {string} url - The URL to fetch data from
 * @param {number} [maxRetries=3] - Maximum number of retry attempts
 * @param {number} [delayMs=1000] - Delay between retries in milliseconds
 * @returns {Promise<any>} - Resolves with the JSON data
 */
async function fetchWithRetry(url, maxRetries = 3, delayMs = 1000) {
    let lastError;

    for (let attempt = 0; attempt <= maxRetries; attempt++) {
        try {
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            lastError = error;

            if (attempt === maxRetries) break;

            console.warn(`Attempt ${attempt + 1} failed: ${error.message}. Retrying in ${delayMs}ms...`);
            await new Promise(resolve => setTimeout(resolve, delayMs));
        }
    }

    throw new Error(`Failed to fetch after ${maxRetries} retries. Last error: ${lastError.message}`);
}

module.exports = { fetchWithRetry };
