# Instructions
# Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.
# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]
def capitals(word):
    return [i for i, l in enumerate(word) if l.isupper()]


if __name__ == "__main__":
    print(capitals("CodEWaRs"))  # [0, 3, 4, 6]
    print(capitals("tEStinG"))  # [1, 2, 6]
    print(capitals("123456"))  # []
