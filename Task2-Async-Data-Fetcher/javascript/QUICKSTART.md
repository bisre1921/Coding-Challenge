# Async Data Fetcher with Retry

A robust JavaScript utility that fetches data from a URL and automatically retries on failure.

## 🚀 Quick Start

### 1. Setup
```bash
cd Task2-Async-Data-Fetcher/javascript
npm install
```

### 2. Run Demo
```bash
npm start
```
This runs `src/index.js` which demonstrates both successful fetching and retry logic on failure.

### 3. Run Tests
```bash
npm test
```
Runs the Jest test suite to verify retry logic and error handling.

## 💻 Usage

```javascript
const { fetchWithRetry } = require('./src/fetcher');

async function getData() {
    try {
        // Fetch with default settings (3 retries, 1s delay)
        const data = await fetchWithRetry('https://api.example.com/data');
        console.log(data);
    } catch (error) {
        console.error('Final failure:', error.message);
    }
}
```

### Custom Configuration
```javascript
// Retry 5 times with 2 seconds delay between attempts
await fetchWithRetry('https://api.example.com/data', 5, 2000);
```

## 📂 Project Structure
```
javascript/
├── src/
│   ├── fetcher.js      # Core logic with async/await & retry loop
│   └── index.js        # Demo script
├── tests/
│   └── fetcher.test.js # Jest unit tests
├── package.json        # Dependencies
└── QUICKSTART.md       # This guide
```

## ✨ Features
- **Async/Await**: Clean, modern asynchronous code.
- **Configurable Retries**: Set max retries and delay duration.
- **Error Handling**: Catches both network errors and HTTP error status codes.
- **Exponential Backoff**: (Optional) Can be easily added to the delay logic.
