# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples
# "foefet" is an anagram of "toffee"
# "Buckethead" is an anagram of "DeathCubeK"
def is_anagram(test, original):
    return {x: test.lower().count(x) for x in test.lower()} == {x: original.lower().count(x) for x in original.lower()}


if __name__ == "__main__":
    print(is_anagram("foefet", "toffee"))  # True
    print(is_anagram("apple", "pale"))  # False
    print(is_anagram("Twoo", "WooT"))  # True
