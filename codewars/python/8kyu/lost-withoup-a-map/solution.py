# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    return [n * 2 for n in a]


if __name__ == "__main__":
    print(maps([1, 2, 3]))  # [2, 4, 6]
    print(maps([1, 4, 5, 6, 2, 3, 9, 10, 12]))  # [2, 8, 10, 12, 4, 6, 18, 20, 24]
    print(maps([65, -12, 0, 32, 43, 55, 4334, 6543]))  # [130, -24, 0, 64, 86, 110, 8668, 13086]
