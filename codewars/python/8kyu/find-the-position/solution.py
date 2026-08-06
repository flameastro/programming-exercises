# When provided with a letter, return its position in the alphabet.
# Input :: "a"
# Output :: "Position of alphabet: 1"
# Note: Only lowercased English letters are tested


def position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(0, 26):
        if alphabet[i] == letter:
            return f"Position of alphabet: {i+1}"


if __name__ == "__main__":
    print(position("a"))  # Position of alphabet: 1
    print(position("z"))  # Position of alphabet: 26
    print(position("m"))  # Position of alphabet: 13
