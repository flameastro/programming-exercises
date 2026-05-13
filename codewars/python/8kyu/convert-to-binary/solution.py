# Task Overview
# Given a non-negative integer b, write a function which returns an integer d such that the binary representation of b is the same as the decimal representation of d.

# Examples:

# n = 1 should return 1
# n = 5 should return 101
# n = 11 should return 1011
def to_binary(n):
    binary = []

    while n != 0:
        binary.append("1" if n % 2 == 1 else "0")
        n //= 2

    return int("".join(list(reversed((binary)))))

if __name__ == "__main__":
    print(to_binary(1))  # 1
    print(to_binary(5))  # 101
    print(to_binary(15))  # 1111
