# Your task is to write function factorial.
def factorial(n):
    s = 1
    
    for i in range(1, n+1):
        s *= i
    
    return s


if __name__ == "__main__":
    print(factorial(3))  # 6
    print(factorial(5))  # 120
    print(factorial(0))  # 1
