# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
# Solution 1
def duplicate_count(text):
    s = 0
    duplicated = []

    for l in text.lower():
        duplicated.append(l)

        if l in duplicated and duplicated.count(l) == 2:
            s += 1

    return s

# Solution 2
def duplicate_count(text):
    text = text.lower()
    lst = []
    [lst.append(l) for l in text if text.count(l) >= 2 and l not in lst]
    return len(lst)


if __name__ == "__main__":
    print(duplicate_count("abcdef"))  # 
    print(duplicate_count("aabbcde"))  # 
    print(duplicate_count("Indivisibilities"))  # 
