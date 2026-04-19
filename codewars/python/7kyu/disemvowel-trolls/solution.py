# Trolls are attacking your comment section! A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat. Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.
# Solution 1
def disemvowel(string):
    return "".join([l for l in string if l.lower() not in "aeiou"])


# Solution 2
def disemvowel(string):
    r = ""

    for l in string:
        if l.lower() not in ["a", "e", "i", "o", "u"]:
            r += l

    return r


if __name__ == "__main__":
    print(disemvowel("This website is for losers LOL!"))  # Ths wbst s fr lsrs LL!
    print(disemvowel("No way this website is very trash HAHAHAH"))  # N wy ths wbst s vry trsh HHHH
    print(disemvowel("Does this website was created by a human? LMAO"))  # Ds ths wbst ws crtd by  hmn? LM
