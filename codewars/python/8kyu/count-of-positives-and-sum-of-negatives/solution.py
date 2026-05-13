# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]
def count_positives_sum_negatives(arr):
    p = sum([1 for n in arr if n > 0])
    s = sum([n for n in arr if n < 0])

    return [p, s] if len(arr) > 0 else []


if __name__ == "__main__":
    print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))  # [10, -65]
    print(count_positives_sum_negatives([-6, 7, 12, 5, 4, 2, 0, 14]))  # [6, -6]
    print(count_positives_sum_negatives([506, -90, 1, 2, 3]))  # [4, -90]
