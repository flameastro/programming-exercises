# In this simple exercise, you will write a function that takes two integers; n and limit; and returns a list of the multiples of n up to and possibly including limit.
# It is guaranteed that n > 0 and limit >= n.
# For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
# Examples
# n = 2; limit = 6 --> [2, 4, 6]
# n = 2; limit = 5 --> [2, 4]
def find_multiples(integer, limit):
    return [x for x in range(integer, limit+1) if x % integer    == 0]

if __name__ == "__main__":
    print(find_multiples(5, 25))  # [5, 10, 15, 20, 25]
    print(find_multiples(2, 27))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
    print(find_multiples(63, 128))  # [63, 126]



