# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.
# For example:
# a = 1
# b = 4
# --> [1, 2, 3, 4]
def between(a,b):
    return [x for x in range(a, b+1)]


if __name__ == "__main__":
    print(between(1, 4))  # [1, 2, 3, 4]
    print(between(2, 7))  # [2, 3, 4, 5, 6, 7]
    print(between(10, 4))  # []
