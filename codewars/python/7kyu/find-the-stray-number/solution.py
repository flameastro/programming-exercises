# This exercise has been solved before but with another way to do. That solution is for tests with a big amount of data, then need a more efficient algorithm. This is a bad algorithm for a big amount of data, so you can find a better solution at: codewars/python/6kyu/find-the-unique-number
# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)
# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

def stray(arr):
    return [x for x in arr if arr.count(x) == 1][0]


if __name__ == "__main__":
    print(stray([1, 1, 2]))  # 2
    print(stray([5, 5, 5, 2, 5, 5, 5, 5]))  # 2
    print(stray([7, 3, 3, 3, 3]))  # 7
