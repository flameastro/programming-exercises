# Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 --> [5,4,3,2,1]
def reverse_seq(n):
    return [d for d in range(n, 0, -1)]


if __name__ == "__main__":
    print(reverse_seq(12))  # [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(reverse_seq(5))  # [5, 4, 3, 2, 1]
    print(reverse_seq(6))  # [6, 5, 4, 3, 2, 1]
