# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# Example
# Input = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
# Solution 1
def alphabet_position(text):
    r = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for l in text.lower():
        if l in alphabet:
            r += f"{alphabet.index(l)+1} "

    return r.strip()

# Solution 2
def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return "".join([f"{str(alphabet.index(r)+1)} " for r in text.lower() if r in alphabet]).strip()


if __name__ == "__main__":
    print(alphabet_position("abcdef"))  # 1 2 3 4 5 6
    print(alphabet_position("This is an example"))  # 20 8 9 19 9 19 1 14 5 24 1 13 16 12 5
    print(alphabet_position("ay2h31"))  # 1 25 8
