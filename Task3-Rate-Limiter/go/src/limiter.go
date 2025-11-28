package src

import (
	"sync"
	"time"
)

// RateLimiter controls request rates per user.
type RateLimiter struct {
	limit    int           // Max requests allowed
	window   time.Duration // Time window duration
	users    map[string]*userBucket
	mu       sync.Mutex    // Protects access to users map
}

// userBucket tracks requests for a single user.
type userBucket struct {
	count     int
	resetTime time.Time
}

// NewRateLimiter creates a new limiter with specified rules.
func NewRateLimiter(limit int, window time.Duration) *RateLimiter {
	return &RateLimiter{
		limit:  limit,
		window: window,
		users:  make(map[string]*userBucket),
	}
}

// Allow checks if a request is allowed for the given user.
func (rl *RateLimiter) Allow(userID string) bool {
	rl.mu.Lock()
	defer rl.mu.Unlock()

	bucket, exists := rl.users[userID]
	now := time.Now()

	// New user or window expired
	if !exists || now.After(bucket.resetTime) {
		rl.users[userID] = &userBucket{
			count:     1,
			resetTime: now.Add(rl.window),
		}
		return true
	}

	// Check limit
	if bucket.count < rl.limit {
		bucket.count++
		return true
	}

	return false
}

// Reset clears all user data (useful for testing).
func (rl *RateLimiter) Reset() {
	rl.mu.Lock()
	defer rl.mu.Unlock()
	rl.users = make(map[string]*userBucket)
}
