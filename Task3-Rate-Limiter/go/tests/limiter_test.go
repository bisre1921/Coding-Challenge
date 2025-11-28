package tests

import (
	"testing"
	"time"

	"github.com/eaglepoint/ratelimiter/src"
)

func TestRateLimiter_Allow(t *testing.T) {
	// 5 requests per 1 second
	limiter := src.NewRateLimiter(5, 1*time.Second)
	userID := "test_user"

	// First 5 should be allowed
	for i := 0; i < 5; i++ {
		if !limiter.Allow(userID) {
			t.Errorf("Request %d should be allowed", i+1)
		}
	}

	// 6th should be blocked
	if limiter.Allow(userID) {
		t.Error("Request 6 should be blocked")
	}
}

func TestRateLimiter_Reset(t *testing.T) {
	// 2 requests per 100ms
	limiter := src.NewRateLimiter(2, 100*time.Millisecond)
	userID := "test_user"

	// Consume limit
	limiter.Allow(userID)
	limiter.Allow(userID)

	// Should be blocked
	if limiter.Allow(userID) {
		t.Error("Should be blocked")
	}

	// Wait for window to expire
	time.Sleep(150 * time.Millisecond)

	// Should be allowed again
	if !limiter.Allow(userID) {
		t.Error("Should be allowed after reset")
	}
}

func TestRateLimiter_MultipleUsers(t *testing.T) {
	limiter := src.NewRateLimiter(1, 1*time.Second)
	
	// User 1 consumes limit
	if !limiter.Allow("user1") {
		t.Error("User 1 should be allowed")
	}
	if limiter.Allow("user1") {
		t.Error("User 1 should be blocked")
	}

	// User 2 should still be allowed (independent tracking)
	if !limiter.Allow("user2") {
		t.Error("User 2 should be allowed")
	}
}
