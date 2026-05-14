# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively. Each function returns one number.
# Examples (Input -> Output)
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# Notes
# You may consider that there will not be any empty arrays/vectors.
# Solution 1
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


# Solution 2
def minimum(arr):
    return list(sorted(arr))[0]

def maximum(arr):
    return list(sorted(arr))[-1]


if __name__ == "__main__":
    print(minimum([1, -9, 0, 12, 4]))  # -9
    print(minimum([3, -2, 9, 17, 7, 13]))  # -2
    print(maximum([-1, 877, 999]))  # 999
