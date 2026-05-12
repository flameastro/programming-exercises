# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0     => [0]
def digitize(n):
    return list(reversed([int(d) for d in str(n)]))


if __name__ == "__main__":
    print(digitize(35231))  # [1, 3, 2, 5, 3]
    print(digitize(23582357))  # [7, 5, 3, 2, 8, 5, 3, 2]
    print(digitize(45762893920))  # [0, 2, 9, 3, 9, 8, 2, 6, 7, 5, 4]
