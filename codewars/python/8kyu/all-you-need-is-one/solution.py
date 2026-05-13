# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# a can contain numbers or strings. x can be either.
# Return true if the array contains the value, false if not.
def check(seq, elem):
    return elem in seq

if __name__ == "__main__":
    print(check([1, 2, 3, 4, 5], 2))  # True
    print(check([0, -1, -2, -3], 4))  # False
    print(check([500, 3732, 382, -3281, 736, 23], 12))  # False
