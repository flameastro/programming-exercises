# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
# Examples:
# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"
def spin_words(sentence):
    final_word = ""

    for word in sentence.split():
        if len(word) >= 5:
            final_word += f"{word[::-1]} "
        else:
            final_word += f"{word} "

    return final_word.strip()


if __name__ == "__main__":
    print(spin_words("CodeWars"))  # sraWedoC
    print(spin_words("Hey fellow warriors"))  # Hey wollef sroirraw
    print(spin_words("This sentence is a sentence"))  # This ecnetnes is a ecnetnes
