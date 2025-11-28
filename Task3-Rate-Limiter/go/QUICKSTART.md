# Rate Limiter (Go)

A thread-safe, in-memory rate limiter implementation in Go.

## 🚀 Quick Start

### 1. Run Demo
```bash
cd Task3-Rate-Limiter/go
go run cmd/demo/main.go
```
go run cmd/demo/main.go
```
This demonstrates blocking requests after the limit is reached and allowing them again after the time window resets.
**Note:** The demo uses a 2-second window (instead of the required 60s) for faster demonstration.

### 2. Run Tests
```bash
go test ./tests -v
```
Runs the test suite to verify logic correctness.

## 💻 Usage

```go
import (
    "time"
    "github.com/eaglepoint/ratelimiter/src"
)

func main() {
    // Create limiter: 5 requests per 60 seconds
    limiter := src.NewRateLimiter(5, 60*time.Second)
    userID := "user_123"

    if limiter.Allow(userID) {
        // Process request
    } else {
        // Return 429 Too Many Requests
    }
}
```

## 📂 Project Structure
```
go/
├── src/
│   ├── limiter.go       # Core logic (Thread-safe)
│   └── main.go          # Demo application
├── tests/
│   └── limiter_test.go  # Unit tests
├── go.mod               # Module definition
└── QUICKSTART.md        # This guide
```

## ✨ Features
- **Thread-Safe**: Uses `sync.Mutex` for concurrent access.
- **User Isolation**: Tracks limits independently per user ID.
- **Auto-Reset**: Automatically resets counts after the time window expires.
- **Clean API**: Simple `Allow(userID)` method.
