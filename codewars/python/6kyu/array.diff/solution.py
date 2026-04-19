# Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

# Solution 1
def array_diff(a, b):
    return [x for x in a if x not in b]


# Solution 2
def array_diff(a, b):
    c = []

    for x in a:
        if x not in b:
            c.append(x)

    return c


if __name__ == "__main__":
    print(array_diff([1, 2], [1]))  # [2]
    print(array_diff([1,2,2], [1]))  # [2, 2]
    print(array_diff([1,2,2], [2]))  # [1]
