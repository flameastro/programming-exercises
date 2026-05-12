# Task
# You get an array of numbers, return the sum of all of the positives ones.

# Example
# [1, -4, 7, 12] => 1 + 7 + 12 = 20 
# Note If there is nothing to sum, the sum is default to 0.


def positive_sum(arr):
    return sum([x for x in arr if x > 0])


if __name__ == "__main__":
    print(positive_sum([1, 2, 3, 4]))  # 10
    print(positive_sum([-1, 4, -2, -5, 12]))  # 16
    print(positive_sum([-6, 0, 12, 15, -40]))  # 27
