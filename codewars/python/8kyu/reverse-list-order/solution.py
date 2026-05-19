# In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]
# Solution 1
def reverse_list(l):
    return list(reversed(l))


# Solution 2
def reverse_list(l):
    return l[::-1]


# Solution 3
def reverse_list(l):
    nl = []
    c = -1

    for _ in l:
        nl.append(l[c])
        c -= 1

    return nl


if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]
    print(reverse_list([5, 4, 8, 2, 1]))  # [1, 2, 8, 4, 5]
    print(reverse_list([9, 2, 0, 7]))  # [7, 0, 2, 9]
