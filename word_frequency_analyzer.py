from collections import Counter
import nltk
from nltk.corpus import stopwords

# Download common english stopwords using nltk library
nltk.download('stopwords')


class WordFrequencyAnalyzer:
    def analyze(self, text):
        """Analyzes the word frequency in the given text, excluding common stopwords"""
        words = text.split()

        # Use list comprehension to filter out common stopwords
        filtered_words = [
            word for word in words if word not in stopwords.words('english')]

        return Counter(filtered_words)
