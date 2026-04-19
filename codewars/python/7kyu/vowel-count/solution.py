# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.
# Solution 1
def get_count(sentence):
    return sum([1 for l in sentence if l.lower() in "aeiou"])


# Solution 2
def get_count(sentence):
    c = 0

    for l in sentence:
        if l.lower() in "aeiou":
            c += 1

    return c


if __name__ == "__main__":
    print(get_count("abcedfg"))  # 2
    print(get_count("one two three four five"))  # 9
    print(get_count("aeiouyp"))  # 5
