# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.
def sum_mix(arr):
    return sum([int(n) for n in arr])


if __name__ == "__main__":
    print(sum_mix([12, "4", 5, 1, 2, "0", "43"]))  # 67
    print(sum_mix(["7", "8", "9"]))  # 24
    print(sum_mix(["15", "-40", 256]))  # 231
