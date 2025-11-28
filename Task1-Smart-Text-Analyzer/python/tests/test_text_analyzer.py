"""Unit Tests for Text Analyzer"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

import unittest
from text_analyzer import TextAnalyzer, analyze_text


class TestTextAnalyzer(unittest.TestCase):
    """Test cases for the TextAnalyzer class."""
    
    def test_example_case(self):
        """Test the exact example from requirements."""
        text = "Full stack developer Technical Assessment"
        result = analyze_text(text)
        
        self.assertEqual(result['word_count'], 5)
        self.assertAlmostEqual(result['average_word_length'], 7.40, places=2)
        self.assertCountEqual(result['longest_words'], ["assessment"])
        self.assertEqual(result['word_frequency']['full'], 1)
        self.assertEqual(result['word_frequency']['stack'], 1)
        self.assertEqual(result['word_frequency']['developer'], 1)
    
    def test_empty_text(self):
        """Test with empty text."""
        analyzer = TextAnalyzer("")
        result = analyzer.analyze()
        
        self.assertEqual(result['word_count'], 0)
        self.assertEqual(result['average_word_length'], 0.0)
        self.assertEqual(result['longest_words'], [])
        self.assertEqual(result['word_frequency'], {})
    
    def test_single_word(self):
        """Test with a single word."""
        analyzer = TextAnalyzer("Hello")
        result = analyzer.analyze()
        
        self.assertEqual(result['word_count'], 1)
        self.assertEqual(result['average_word_length'], 5.0)
        self.assertEqual(result['longest_words'], ["hello"])
        self.assertEqual(result['word_frequency'], {"hello": 1})
    
    def test_case_insensitive(self):
        """Test case-insensitive word frequency."""
        analyzer = TextAnalyzer("The THE the")
        result = analyzer.analyze()
        
        self.assertEqual(result['word_count'], 3)
        self.assertEqual(result['word_frequency']['the'], 3)
    
    def test_punctuation_handling(self):
        """Test that punctuation is properly removed."""
        analyzer = TextAnalyzer("Hello, world! How are you?")
        result = analyzer.analyze()
        
        self.assertEqual(result['word_count'], 5)
        self.assertIn("hello", result['word_frequency'])
        self.assertIn("world", result['word_frequency'])
        self.assertNotIn(",", result['word_frequency'])
        self.assertNotIn("!", result['word_frequency'])
    
    def test_multiple_longest_words(self):
        """Test when multiple words tie for longest."""
        analyzer = TextAnalyzer("cat dog bat")
        result = analyzer.analyze()
        
        self.assertEqual(len(result['longest_words']), 3)
        self.assertCountEqual(result['longest_words'], ["cat", "dog", "bat"])
    
    def test_average_word_length_precision(self):
        """Test that average is rounded to 2 decimal places."""
        analyzer = TextAnalyzer("a bb ccc")
        result = analyzer.analyze()
        
        self.assertEqual(result['average_word_length'], 2.0)
        
        analyzer2 = TextAnalyzer("ab abc")
        result2 = analyzer2.analyze()
        
        self.assertEqual(result2['average_word_length'], 2.5)
    
    def test_word_frequency_accuracy(self):
        """Test word frequency counting."""
        analyzer = TextAnalyzer("apple banana apple cherry banana apple")
        result = analyzer.analyze()
        
        self.assertEqual(result['word_frequency']['apple'], 3)
        self.assertEqual(result['word_frequency']['banana'], 2)
        self.assertEqual(result['word_frequency']['cherry'], 1)
    
    def test_special_characters(self):
        """Test handling of special characters."""
        analyzer = TextAnalyzer("Hello@world #test $money")
        result = analyzer.analyze()
        
        self.assertEqual(result['word_count'], 4)
        self.assertIn("hello", result['word_frequency'])
        self.assertIn("world", result['word_frequency'])
        self.assertIn("test", result['word_frequency'])
        self.assertIn("money", result['word_frequency'])
    
    def test_numbers_in_text(self):
        """Test handling of numbers."""
        analyzer = TextAnalyzer("Hello 123 world 456")
        result = analyzer.analyze()
        
        self.assertEqual(result['word_count'], 4)
        self.assertIn("123", result['word_frequency'])
    
    def test_longest_words_order(self):
        """Test that longest words maintain order of first appearance."""
        analyzer = TextAnalyzer("zebra apple tiger")
        result = analyzer.analyze()
        
        self.assertEqual(result['longest_words'], ["zebra", "apple", "tiger"])
    
    def test_whitespace_handling(self):
        """Test handling of multiple spaces and newlines."""
        analyzer = TextAnalyzer("hello    world\n\ntest")
        result = analyzer.analyze()
        
        self.assertEqual(result['word_count'], 3)
        self.assertIn("hello", result['word_frequency'])
        self.assertIn("world", result['word_frequency'])
        self.assertIn("test", result['word_frequency'])


class TestAnalyzeTextFunction(unittest.TestCase):
    """Test the convenience function."""
    
    def test_convenience_function(self):
        """Test the analyze_text convenience function."""
        result = analyze_text("quick test")
        
        self.assertIsInstance(result, dict)
        self.assertIn('word_count', result)
        self.assertIn('average_word_length', result)
        self.assertIn('longest_words', result)
        self.assertIn('word_frequency', result)
        self.assertEqual(result['word_count'], 2)


if __name__ == '__main__':
    unittest.main()
