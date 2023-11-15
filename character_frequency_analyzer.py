from collections import Counter


class CharacterFrequencyAnalyzer:
    def analyze(self, text):
        """Analyzes the frequency of each character in the given text"""
        return Counter(text)

    def optimized_analyze(self, text):
        """Analyzes the frequency of each alphabetic character in the given text, case-insensitive"""
        # Use generator expression to create a Counter of lowercase alphabetic characters
        return Counter(char.lower() for char in text if char.isalpha())
