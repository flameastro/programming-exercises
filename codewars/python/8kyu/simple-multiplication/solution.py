# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9

if __name__ == "__main__":
    print(simple_multiplication(43))  # 387
    print(simple_multiplication(12))  # 96
    print(simple_multiplication(5))  # 45
