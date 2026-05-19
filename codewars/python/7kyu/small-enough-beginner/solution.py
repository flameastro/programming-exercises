# You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.
# You can assume all values in the array are numbers.
def small_enough(array, limit):
    for l in array:
        if l > limit:
            return False

    return True


if __name__ == "__main__":
    print(small_enough([66, 101], 200))  # True
    print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100))  # False
    print(small_enough([101, 45, 75, 105, 99, 107], 107))  # True

