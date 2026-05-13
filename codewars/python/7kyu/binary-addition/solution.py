# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
# The binary number returned should be a string.
# Examples:(Input1, Input2 --> Output (explanation)))
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
def add_binary(a, b):
    binary = []

    s = a + b
    while s != 0:
        binary.append("1" if s % 2 == 1 else "0")
        s //= 2

    return "".join(list(reversed((binary))))

if __name__ == "__main__":
    print(add_binary(1, 1))  # 10
    print(add_binary(5, 9))  # 1110
    print(add_binary(15, 2))  # 10001
