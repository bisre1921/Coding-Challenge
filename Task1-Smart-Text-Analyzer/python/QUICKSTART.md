# Quick Start Guide

## Get Started in 30 Seconds

### 1. Navigate to the source directory
```bash
cd Task1-Smart-Text-Analyzer/python/src
```

### 2. Run the interactive analyzer
```bash
python3 main.py
```

### 3. Enter your text
```
Enter the text you want to analyze.
(Press Enter twice or type 'quit' to exit)

Full stack developer Technical Assessment

```

### 4. View results!
```
============================================================
TEXT ANALYSIS RESULTS
============================================================

Word Count: 5
Average Word Length: 7.40 characters

Longest Words (1 word(s)):
  • assessment (10 characters)

Word Frequency (Top 10):
  • assessment: 1
  • developer: 1
  • full: 1
  • stack: 1
  • technical: 1
============================================================
```

## 🧪 Run Tests

```bash
cd Task1-Smart-Text-Analyzer/python/tests
python3 test_text_analyzer.py -v
```

All 13 tests should pass!

## 🎬 See Demo

```bash
cd Task1-Smart-Text-Analyzer/python/src
python3 demo.py
```

This shows 7 different use cases with example outputs.

## 💻 Use in Your Code

```python
from text_analyzer import analyze_text

result = analyze_text("Your text here")
print(result['word_count'])
print(result['average_word_length'])
print(result['longest_words'])
print(result['word_frequency'])
```

## Project Structure
```
python/
├── src/
│   ├── text_analyzer.py  # Core logic
│   ├── formatter.py      # Output formatting
│   ├── main.py          # Interactive CLI
│   └── demo.py          # Feature demos
├── tests/
│   └── test_text_analyzer.py  # 13 test cases
└── QUICKSTART.md        # This file
```

## What It Does

* Counts total words  
* Calculates average word length (2 decimal precision)  
* Finds all longest words (handles ties)  
* Analyzes word frequency (case-insensitive)  
* Handles punctuation correctly  
* Processes special characters  
* Works with multi-line text  

## Next Steps
