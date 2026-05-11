# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1 ^ 2 + 2 ^ 2 + 2 ^ 2 = 9

# Solution 1
def square_sum(numbers):
    return sum([n ** 2 for n in numbers])

# Solution 2
def square_sum(numbers):
    s = 0

    for n in numbers:
        s += n ** 2

    return s


if __name__ == "__main__":
    print(square_sum([1, 2, 2]))  # 9
    print(square_sum([3, 2, 1]))  # 14
    print(square_sum([6, 6, 6]))  # 108
