"""Text Analyzer Module"""

from typing import Dict, List
from collections import Counter
import re


class TextAnalyzer:
    """Comprehensive text analyzer that extracts various metrics from text."""
    
    def __init__(self, text: str):
        self.text = text
        self._words: List[str] = []
        self._process_text()
    
    def _process_text(self) -> None:
        """Process and normalize the input text into individual words."""
        cleaned_text = re.sub(r'[^\w\s]', ' ', self.text)
        self._words = [word.lower() for word in cleaned_text.split() if word.strip()]
    
    def get_word_count(self) -> int:
        """Calculate the total number of words in the text."""
        return len(self._words)
    
    def get_average_word_length(self) -> float:
        """Calculate the average length of words, rounded to 2 decimal places."""
        if not self._words:
            return 0.0
        
        total_length = sum(len(word) for word in self._words)
        average = total_length / len(self._words)
        return round(average, 2)
    
    def get_longest_words(self) -> List[str]:
        """Find the longest word(s) in the text. Returns all if tied."""
        if not self._words:
            return []
        
        max_length = max(len(word) for word in self._words)
        longest_words = {}
        for word in self._words:
            if len(word) == max_length and word not in longest_words:
                longest_words[word] = None
        
        return list(longest_words.keys())
    
    def get_word_frequency(self) -> Dict[str, int]:
        """Calculate the frequency of each word (case-insensitive)."""
        return dict(Counter(self._words))
    
    def analyze(self) -> Dict:
        """Perform complete text analysis and return all metrics."""
        return {
            "word_count": self.get_word_count(),
            "average_word_length": self.get_average_word_length(),
            "longest_words": self.get_longest_words(),
            "word_frequency": self.get_word_frequency()
        }


def analyze_text(text: str) -> Dict:
    """Convenience function to analyze text in a single call."""
    analyzer = TextAnalyzer(text)
    return analyzer.analyze()
