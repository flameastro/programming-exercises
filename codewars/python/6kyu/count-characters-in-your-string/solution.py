# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.
# Solution 1
def count(s):
    r = {}

    for l in s:
        if l not in r:
            r[l] = s.count(l)

    return r


# Solution 2
def count(s):
    lst = []
    r = {l: s.count(l) for l in s if l not in lst}
    return r


if __name__ == "__main__":
    print(count("aba"))  # {'a': 2, 'b': 1}
    print(count("example of input"))  # {'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 2, 'l': 1, ' ': 2, 'o': 1, 'f': 1, 'i': 1, 'n': 1, 'u': 1, 't': 1}
    print(count("and linus said: for personal purposes only :D"))  # {'a': 3, 'n': 4, 'd': 2, ' ': 7, 'l': 3, 'i': 2, 'u': 2, 's': 5, ':': 2, 'f': 1, 'o': 4, 'r': 3, 'p': 3, 'e': 2, 'y': 1, 'D': 1}
