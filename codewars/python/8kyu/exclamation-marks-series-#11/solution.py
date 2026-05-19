# Description:
# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

# Examples
# "Hi!" --> "H!!"
# "!Hi! Hi!" --> "!H!! H!!"
# "aeiou" --> "!!!!!"
# "ABCDE" --> "!BCD!"
def replace_exclamation(st):
    return "".join(["!" if l in "aeiouAEIOU" else l for l in st])


if __name__ == "__main__":
    print(replace_exclamation("HI!"))  # H!!
    print(replace_exclamation("Hello, World!"))  # H!ll!, W!rld!
    print(replace_exclamation("Exclamation Marks?"))  # !xcl!m!t!!n M!rks?
