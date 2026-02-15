'''
Tutorial Test Week 10 - Question 2
Word Frequency Analyzer with Ordered Access (BST Application)

@Author: Alok More
'''


class WordAnalyzer:
    """
    Analyzes text and maintains word frequencies in alphabetical order.
    Uses Binary Search Tree principles for efficient ordered operations.
    """
    
    def __init__(self):
        """Initialize an empty word analyzer"""
        # TODO: Initialize your data structure here
        # Hint: You'll need to store words and their frequencies in order
        pass
    
    def add_text(self, text):
        """
        Process text and count word frequencies.
        Converts to lowercase, splits on whitespace, ignores empty strings.
        
        Args:
            text (str): The text to analyze
        """
        # TODO: Implement text processing and word counting
        # Remember to:
        # - Convert to lowercase
        # - Split on whitespace
        # - Ignore empty strings
        # - Increment count for each word
        pass
    
    def get_frequency(self, word):
        """
        Get the frequency count for a given word.
        
        Args:
            word (str): The word to look up
        
        Returns:
            int: The frequency count (0 if word not found)
        """
        # TODO: Implement frequency lookup
        pass
    
    def get_all_words_sorted(self):
        """
        Get all words sorted alphabetically.
        
        Returns:
            list: List of (word, frequency) tuples sorted by word
        """
        # TODO: Implement in-order traversal
        # Return format: [("apple", 3), ("banana", 1), ...]
        pass
    
    def get_words_in_range(self, start_word, end_word):
        """
        Get all words alphabetically between start_word and end_word (inclusive).
        
        Args:
            start_word (str): Lower bound word
            end_word (str): Upper bound word
        
        Returns:
            list: List of (word, frequency) tuples sorted by word
        """
        # TODO: Implement range query
        # Return format: [("apple", 3), ("banana", 1), ...]
        pass
    
    def get_most_frequent_word(self):
        """
        Get the most frequent word.
        If multiple words have same max frequency, return any one.
        
        Returns:
            tuple or None: (word, frequency) or None if analyzer is empty
        """
        # TODO: Implement finding most frequent word
        # Hint: Need to traverse all words to find max frequency
        pass
    
    def get_least_frequent_word(self):
        """
        Get the least frequent word.
        If multiple words have same min frequency, return any one.
        
        Returns:
            tuple or None: (word, frequency) or None if analyzer is empty
        """
        # TODO: Implement finding least frequent word
        # Hint: Need to traverse all words to find min frequency
        pass
    
    def count_unique_words(self):
        """
        Get the total number of unique words.
        
        Returns:
            int: Number of unique words
        """
        # TODO: Implement unique word count
        pass


# Simple testing code
if __name__ == "__main__":
    print("Testing WordAnalyzer Class")
    print("=" * 50)
    
    analyzer = WordAnalyzer()
    
    # Test 1: Add text
    print("\n1. Adding text:")
    text1 = "the quick brown fox jumps over the lazy dog"
    analyzer.add_text(text1)
    print(f"Added: '{text1}'")
    
    # Test 2: Add more text
    print("\n2. Adding more text:")
    text2 = "the fox and the dog are friends"
    analyzer.add_text(text2)
    print(f"Added: '{text2}'")
    
    # Test 3: Get frequency
    print("\n3. Getting word frequencies:")
    print(f"'the' frequency: {analyzer.get_frequency('the')}")
    print(f"'fox' frequency: {analyzer.get_frequency('fox')}")
    print(f"'missing' frequency: {analyzer.get_frequency('missing')}")
    
    # Test 4: Count unique words
    print("\n4. Unique word count:")
    print(f"Total unique words: {analyzer.count_unique_words()}")
    
    # Test 5: All words sorted
    print("\n5. All words (sorted alphabetically):")
    all_words = analyzer.get_all_words_sorted()
    for word, freq in all_words:
        print(f"  {word}: {freq}")
    
    # Test 6: Words in range
    print("\n6. Words from 'dog' to 'lazy':")
    print(analyzer.get_words_in_range("dog", "lazy"))
    
    # Test 7: Most and least frequent
    print("\n7. Most and least frequent words:")
    print(f"Most frequent: {analyzer.get_most_frequent_word()}")
    print(f"Least frequent: {analyzer.get_least_frequent_word()}")
    
    # Test 8: Empty analyzer
    print("\n8. Testing empty analyzer:")
    empty_analyzer = WordAnalyzer()
    print(f"Empty count: {empty_analyzer.count_unique_words()}")
    print(f"Empty most frequent: {empty_analyzer.get_most_frequent_word()}")
    
    print("\n" + "=" * 50)
    print("Testing complete!")
