import re


class PalindromeChecker:
    @staticmethod
    def is_palindrome(text, word):
        """Checks if the given word is a palindrome, case-insensitive"""
        words_in_text = text.split()

        # Notify if the word is not found in the text
        if word not in words_in_text:
            print(f"The word '{word}' is not found in the text!")

        # Compare the lowercase word with its reversed version
        return word.lower() == word.lower()[::-1]
