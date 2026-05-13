# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
def grow(arr):
    s = 1
    for x in arr:
        s *= x

    return s

if __name__ == "__main__":
    print(grow([1, 2, 3, 4]))  # 24
    print(grow([4, 5, 2]))  # 40
    print(grow([7, 6, 4, 3, 9]))  # 4536
