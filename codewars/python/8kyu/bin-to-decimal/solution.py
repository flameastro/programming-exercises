# Complete the function which converts a binary number (given as a string) to a decimal number.
def bin_to_decimal(inp):
    m = 1
    s = 0
    for n in list(inp)[::-1]:
        if int(n) == 1:
            s += m

        m *= 2

    return s

if __name__ == "__main__":
    print(bin_to_decimal("100"))  # 4
    print(bin_to_decimal("101"))  # 5
    print(bin_to_decimal("110"))  # 6
