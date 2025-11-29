# EaglePoint Technical Assessment

This repository contains my completed solutions for three independent technical tasks. Each task is implemented in a different programming language (Python, JavaScript, and Go), and each has its own folder, source code, and quickstart guide.

## Task 1 - Smart Text Analyzer (Python)

This task was about creating a small program that analyzes a block of text and returns useful metrics such as word count, average word length, the longest words, and word frequencies.

To keep the project clean and easy to extend, I used a simple object-oriented structure. The text-processing logic, output formatting, and command-line interaction are all separated into small, focused components.
Regex-based tokenization is used to handle punctuation and case differences.
I also added unit tests to cover various edge cases, including empty text and extra punctuation.

---

## Task 2 - Async Data Fetcher (JavaScript)

For this task, I built a function that fetches data from a URL and automatically retries if the request fails.

The implementation is based on modern `async/await` patterns for clarity.
A retry loop handles failures, with a short delay before each new attempt.
Both network errors and HTTP errors (like 404 or 500) are handled gracefully.
I also included Jest tests that use mocked fetch calls so the retry logic can be tested without hitting real external APIs.

---

## Task 3 - Rate Limiter (Go)

This task required implementing a simple rate-limiting system that allows a user to make up to five requests every sixty seconds.

I built a small, thread-safe rate limiter using Go’s `sync.Mutex` to ensure correct behavior when accessed concurrently.
The logic is based on a fixed-window approach: each user has a counter and a reset timestamp.
The project is structured using idiomatic Go layout, with the main logic in a library package and a demo app in a `cmd` folder.
Unit tests verify the limit, the blocking behavior, and the reset after the time window passes.

---

## How to Run the Tasks

Each task includes a `QUICKSTART.md` file inside its folder with exact setup and run instructions.

You can jump into a task by navigating to its directory:

* Task 1 (Python): `Task1-Smart-Text-Analyzer/python`
* Task 2 (JavaScript): `Task2-Async-Data-Fetcher/javascript`
* Task 3 (Go): `Task3-Rate-Limiter/go`

---
