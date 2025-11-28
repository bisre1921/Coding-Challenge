package main

import (
	"fmt"
	"time"

	"github.com/eaglepoint/ratelimiter/src"
)

func main() {
	fmt.Println("Rate Limiter Demo")
	fmt.Println("-----------------")

	// Limit: 5 requests per 2 seconds (shortened for demo)
	limiter := src.NewRateLimiter(5, 2*time.Second)
	userID := "user_123"

	fmt.Printf("Config: %d requests per 2 seconds\n\n", 5)

	// Simulate 10 rapid requests
	for i := 1; i <= 10; i++ {
		allowed := limiter.Allow(userID)
		status := "Allowed"
		if !allowed {
			status = "Blocked"
		}
		fmt.Printf("Request %d: %s\n", i, status)
		time.Sleep(100 * time.Millisecond)
	}

	fmt.Println("\nWaiting for window reset (2s)...")
	time.Sleep(2 * time.Second)

	// Try again after reset
	if limiter.Allow(userID) {
		fmt.Println("Request after reset: Allowed")
	} else {
		fmt.Println("Request after reset: Blocked")
	}
}
