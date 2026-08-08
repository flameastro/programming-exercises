# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.
# If the whole array is consecutive then return null.
# The array will always have at least 2 elements and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!
def first_non_consecutive(arr):
    for i, _ in enumerate(arr):
        if i != len(arr)-1 and arr[i+1] - arr[i] >= 2:
            return arr[i+1]


if __name__ == "__main__":
    print(first_non_consecutive([1,2,3,4,6,7,8]))  # 6
    print(first_non_consecutive([1, 3, 4, 5, 6, 7, 8]))  # 3
    print(first_non_consecutive([4, 5, 6, 7, 8, 9, 11, 12]))  # 11
