# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false
# Solution 1
def xo(s):
    return len([x for x in s.lower() if x == "x"]) == len([o for o in s.lower() if o == "o"])


# Solution 2
def xo(s):
    xs = 0
    os = 0

    for l in s.lower():
        if l == "x":
            xs += 1
        elif l == "o":
            os += 1

    return xs == os

if __name__ == "__main__":
    print(xo("ooxx"))  # True
    print(xo("xooxx"))  # False
    print(xo("zpzpzpp"))  # True
