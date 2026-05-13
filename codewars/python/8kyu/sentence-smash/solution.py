# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!
# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
# Assumptions
# You can assume that you are only given words.
# You cannot assume the size of the array.
# You can assume that you do get an array.
# What We're Testing
# We're testing basic loops and string manipulation. This is for beginners who are just learning loops and string manipulation.
# Disclaimer
# This is for beginners so we want to test basic loops and string manipulation.
def smash(words):
    return " ".join(words)


if __name__ == "__main__":
    print(smash(["hello", "world", "this", "is", "great"]))  # 
    print(smash(["python", "javascript", "java", "is", "all", "programming", "languages"]))  # 
    print(smash(["I", "said", "programming", "not", "just", "languages!"]))  # 
