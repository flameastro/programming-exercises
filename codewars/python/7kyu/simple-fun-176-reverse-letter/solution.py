# Task
# Given a string str, reverse it and omit all non-alphabetic characters.
# Example
# For str = "krishan", the output should be "nahsirk".
# For str = "ultr53o?n", the output should be "nortlu".
# Input/Output
# [input] string str
# A string consists of lowercase latin letters, digits and symbols.
# [output] a string
def reverse_letter(st):
    return "".join([l for l in st[::-1] if l.isalpha()])


if __name__ == "__main__":
    print(reverse_letter("test"))  # tset
    print(reverse_letter("python"))  # nohtyp
    print(reverse_letter("codewars"))  # srawedoc
