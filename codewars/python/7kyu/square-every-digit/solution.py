# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.
# Happy Coding!
# Solution 1
def square_digits(num):
    n = ""
    for d in str(num):
        n += str(int(d) ** 2)

    return int(n)


# Solution 2
def square_digits(num):
    return int("".join([str(int(d) ** 2) for d in str(num)]))


if __name__ == "__main__":
    print(square_digits(9119))  # 811181
    print(square_digits(4221))  # 16442
    print(square_digits(332))  # 994