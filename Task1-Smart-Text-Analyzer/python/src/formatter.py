"""Output Formatter Module"""

from typing import Dict
import json


class ResultFormatter:
    """Formats analysis results for display."""
    
    @staticmethod
    def to_json(result: Dict, indent: int = 2) -> str:
        """Format result as JSON string."""
        return json.dumps(result, indent=indent, ensure_ascii=False)
    
    @staticmethod
    def to_pretty_text(result: Dict) -> str:
        """Format result as human-readable text."""
        lines = [
            "=" * 60,
            "TEXT ANALYSIS RESULTS",
            "=" * 60,
            f"\nWord Count: {result['word_count']}",
            f"Average Word Length: {result['average_word_length']:.2f} characters",
            f"\nLongest Words ({len(result['longest_words'])} word(s)):",
        ]
        
        for word in result['longest_words']:
            lines.append(f"  • {word} ({len(word)} characters)")
        
        lines.append(f"\nWord Frequency (Top 10):")
        sorted_freq = sorted(
            result['word_frequency'].items(),
            key=lambda x: (-x[1], x[0])
        )
        
        for word, count in sorted_freq[:10]:
            lines.append(f"  • {word}: {count}")
        
        if len(sorted_freq) > 10:
            lines.append(f"  ... and {len(sorted_freq) - 10} more")
        
        lines.append("=" * 60)
        
        return "\n".join(lines)
