# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, return 0.
# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2
# Input: [-2.398]
# Output: -2.398
# Input: []
# Output: 0
# Assumptions
# You can assume that you are given a (possibly empty) valid array containing only numbers.
# What We're Testing
# We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
# Advanced users may find this extremely easy and can easily write this in one line.
# Solution 1
def sum_array(a):
    return sum(a)


# Solution 2
def sum_array(a):
    s = 0

    for n in a:
        s += n

    return s


if __name__ == "__main__":
    print(sum_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 55
    print(sum_array([5, -2, -12, 5, 4, 4, 6]))  # 10
    print(sum_array([0, -9]))  # -9
