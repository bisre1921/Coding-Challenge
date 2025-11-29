"""Main Entry Point - Interactive CLI for Text Analyzer"""

import sys
from typing import Optional
from text_analyzer import analyze_text
from formatter import ResultFormatter


class TextAnalyzerCLI:
    """Command-line interface for the Text Analyzer."""
    
    def __init__(self):
        self.formatter = ResultFormatter()
    
    def get_user_input(self) -> Optional[str]:
        """Prompt user for text input."""
        print("\n" + "=" * 60)
        print("SMART TEXT ANALYZER")
        print("=" * 60)
        print("\nEnter the text you want to analyze.")
        print("(Press Enter twice or type 'quit' to exit)\n")
        
        lines = []
        while True:
            try:
                line = input()
                if line.lower() == 'quit':
                    return None
                if not line and lines:
                    break
                if line:
                    lines.append(line)
            except (EOFError, KeyboardInterrupt):
                print("\n\nOperation cancelled.")
                return None
        
        return " ".join(lines)
    
    def display_result(self, result: dict, format_type: str = 'pretty') -> None:
        """Display analysis results."""
        print("\n")
        if format_type == 'json':
            print(self.formatter.to_json(result))
        else:
            print(self.formatter.to_pretty_text(result))
    
    def run(self) -> None:
        """Run the interactive text analyzer CLI."""
        while True:
            text = self.get_user_input()
            
            if text is None:
                print("\nThank you for using Smart Text Analyzer!")
                break
            
            if not text.strip():
                print("\  No text provided. Please enter some text.\n")
                continue
            
            result = analyze_text(text)
            self.display_result(result, format_type='pretty')
            
            print("\n" + "-" * 60)
            try:
                choice = input("\nAnalyze another text? (yes/no): ").strip().lower()
                if choice not in ['yes', 'y']:
                    print("\nThank you for using Smart Text Analyzer!")
                    break
            except (EOFError, KeyboardInterrupt):
                print("\n\nThank you for using Smart Text Analyzer!")
                break


def main():
    """Main entry point for the application."""
    cli = TextAnalyzerCLI()
    cli.run()


if __name__ == "__main__":
    main()
