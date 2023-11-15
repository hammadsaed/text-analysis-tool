from text_cleaner import TextCleaner
from word_frequency_analyzer import WordFrequencyAnalyzer
from character_frequency_analyzer import CharacterFrequencyAnalyzer
from palindrome_checker import PalindromeChecker


class TextAnalysisTool:
    def __init__(self, text):
        """Initialize the TextAnalysisTool with the given text"""
        self.text = text

    def analyze(self):
        """Analyze the text for word and character frequencies after cleaning"""
        cleaned_text = TextCleaner.remove_punctuation(self.text)
        cleaned_text = TextCleaner.to_lower_case(cleaned_text)

        word_analyzer = WordFrequencyAnalyzer()
        char_analyzer = CharacterFrequencyAnalyzer()

        word_frequency = word_analyzer.analyze(cleaned_text)
        char_frequency = char_analyzer.analyze(cleaned_text)

        return word_frequency, char_frequency

    def top_n_words(self, n):
        """Get the top N words in the text based on frequency"""
        word_analyzer = WordFrequencyAnalyzer()
        word_frequency = word_analyzer.analyze(self.text)
        return word_frequency.most_common(n)

    def is_palindrome(self, word):
        """Check if the given word is a palindrome in the text"""
        return PalindromeChecker.is_palindrome(self.text, word)
