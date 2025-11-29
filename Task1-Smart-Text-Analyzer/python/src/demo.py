#!/usr/bin/env python3
"""Demonstration script showing all features of the Text Analyzer."""

from text_analyzer import analyze_text
from formatter import ResultFormatter

def demo():
    """Run demonstration of text analyzer features."""
    formatter = ResultFormatter()
    
    print("=" * 70)
    print("SMART TEXT ANALYZER - FEATURE DEMONSTRATION")
    print("=" * 70)
    
    # Demo 1: Basic analysis
    print("\n DEMO 1: Basic Text Analysis")
    print("-" * 70)
    text1 = "Full stack developer Technical Assessment"
    print(f"Input: \"{text1}\"")
    result1 = analyze_text(text1)
    print(formatter.to_pretty_text(result1))
    
    # Demo 2: Case insensitivity
    print("\n\n DEMO 2: Case-Insensitive Analysis")
    print("-" * 70)
    text2 = "Python PYTHON python PyThOn"
    print(f"Input: \"{text2}\"")
    result2 = analyze_text(text2)
    print(f"\nAll instances counted as 'python': {result2['word_frequency']['python']} times")
    
    # Demo 3: Punctuation handling
    print("\n\n DEMO 3: Punctuation Handling")
    print("-" * 70)
    text3 = "Hello, world! How are you? I'm fine, thank you."
    print(f"Input: \"{text3}\"")
    result3 = analyze_text(text3)
    print(formatter.to_pretty_text(result3))
    
    # Demo 4: Word frequency
    print("\n\ DEMO 4: Word Frequency Analysis")
    print("-" * 70)
    text4 = "apple banana apple cherry banana apple grape banana apple"
    print(f"Input: \"{text4}\"")
    result4 = analyze_text(text4)
    print("\nWord Frequency:")
    sorted_freq = sorted(result4['word_frequency'].items(), key=lambda x: -x[1])
    for word, count in sorted_freq:
        print(f"  {word}: ({count})")
    
    # Demo 5: JSON output
    print("\n\ DEMO 5: JSON Output Format")
    print("-" * 70)
    text5 = "JSON output example"
    print(f"Input: \"{text5}\"")
    result5 = analyze_text(text5)
    print("\nJSON Format:")
    print(formatter.to_json(result5))
    
    print("\n" + "=" * 70)

    
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\nRun 'python3 main.py' for interactive mode!")
    print()


if __name__ == "__main__":
    demo()
