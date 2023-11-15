import os
from text_analysis_tool import TextAnalysisTool


def get_user_input():
    """Get user input for document path and stop words"""
    document_path = input("Enter the path of the text document: ")
    return document_path


def choose_default_input():
    """Choose the default input file if the provided path is not found"""
    default_input_path = "default_input.txt"
    print(
        f"File not found at the entered path. Using default input from {default_input_path} for analysis")
    return default_input_path


if __name__ == "__main__":
    # Get user input for document path
    document_path = get_user_input()

    # Check if the document path is valid, otherwise use default
    if not os.path.isfile(document_path) or not document_path.endswith('.txt'):
        document_path = choose_default_input()

    # Create an instance of the TextAnalysisTool
    text_analyzer = TextAnalysisTool(text='')

    # Read text from the specified file
    with open(document_path, 'r') as file:
        text_analyzer.text = file.read()

    # Word and Character Frequency Analysis
    word_frequency_result, character_frequency_result = text_analyzer.analyze()
    print("\nWord Frequency Analysis:")
    print(word_frequency_result)

    print("\nCharacter Frequency Analysis:")
    print(character_frequency_result)

    # Top N Words
    n = 3
    print(f"\nTop {n} Words:")
    top_n_words_result = text_analyzer.top_n_words(n)
    print(top_n_words_result)

    # Palindrome Check
    word_to_check = input("\nEnter a word to check for palindrome: ")
    print(
        f"Is '{word_to_check}' a Palindrome? {text_analyzer.is_palindrome(word_to_check)}")
