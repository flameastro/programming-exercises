# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.
def high(string):
    string = string.lower().split()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = 0
    higher = []

    for f in string:
        for l in f:
            s += alphabet.index(l)+1

        higher.append(s)
        s = 0

    return string[higher.index(max(higher))]


if __name__ == "__main__":
    print(high("abad"))  # abad
    print(high("man i need a taxi up to ubud"))  # taxi
    print(high("what time are we climbing up the volcano"))  # volcano
