# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
def reverse_words(text):
    return " ".join([t[::-1] for t in text.split(" ")])


if __name__ == "__main__":
    print(reverse_words("123 456 789"))  # 321 654 987
    print(reverse_words("ABC DEF GH"))  # CBA FED HG
    print(reverse_words("This is an example!"))  # sihT si na !elpmaxe
