
# In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

# Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

# More details about factorial can be found here.

def factorial(n):
    f = 1

    for i in range(1, n+1):
        f *= i

    return f


if __name__ == "__main__":
    print(factorial(3))  # 6
    print(factorial(5))  # 120
    print(factorial(0))  # 1
