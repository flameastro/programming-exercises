# Factors are numbers you can multiply together to get another number.
# 2 and 3 are factors of 6 because: 2 * 3 = 6
# You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
# You can use the mod operator (%) in most languages to check for a remainder
# For example 2 is not a factor of 7 because: 7 % 2 = 1
# Note: base is a non-negative number, factor is a positive number.
def check_for_factor(base, factor):
    return base % factor == 0


if __name__ == "__main__":
    print(check_for_factor(7, 6))  # False
    print(check_for_factor(12, 4))  # True
    print(check_for_factor(45, 9))  # True

