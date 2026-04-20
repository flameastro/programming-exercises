# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
# Solution 1
def find_short(s):
    return min([len(l) for l in s.split()])

# Solution 2
def find_short(s):
    shortest = 0

    for pos, l in enumerate(s.split()):
        if pos == 0:
            shortest = len(l)
        else:
            if shortest > len(l):
                shortest = len(l)

    return shortest


if __name__ == "__main__":
    print(find_short("Python and JavaScript are sick"))  # 3
    print(find_short("i want to travel the world writing code one day"))  # 1
    print(find_short("Please Java compile this code ABRAHADABRA!"))  # 4
