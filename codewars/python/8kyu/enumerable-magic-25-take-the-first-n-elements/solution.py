# Create a function that accepts a list/array and a number n, and returns a list/array of the first n elements from the list/array.
def take(arr,n):
    return arr[:n]


if __name__ == "__main__":
    print(take([1, 2, 3, 4, 5], 3))  # [1, 2, 3]
    print(take([5, 6, 7], 9))  # [5, 6, 7]
    print(take([56, 43, 65, 12, 54, 65, 87, 32, 68, 65, 54], 12))  # [56, 43, 65, 12, 54, 65, 87, 32, 68, 65, 54]
