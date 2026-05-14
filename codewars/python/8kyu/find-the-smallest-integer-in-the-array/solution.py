# Given an array of integers your solution should find the smallest integer.
# For example:
# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.
# Solution 1
def find_smallest_int(arr):
    return min(arr)


# Solution 2
def find_smallest_int(arr):
    return list(sorted(arr))[0]


if __name__ == "__main__":
    print(find_smallest_int([78, 56, -2, 12, 8, -33]))  # -33
    print(find_smallest_int([34, 15, 88, 2]))  # 2
    print(find_smallest_int([34, -345, -1, 100]))  # -345
