import string


class TextCleaner:
    @staticmethod
    def remove_punctuation(text):
        """Removes punctuation from the given text"""
        translator = str.maketrans("", "", string.punctuation)
        return text.translate(translator)

    @staticmethod
    def to_lower_case(text):
        """Converts the given text to lowercase"""
        return text.lower()
