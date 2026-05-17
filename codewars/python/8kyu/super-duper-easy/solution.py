# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".
def problem(a):
    return "Error" if isinstance(a, str) else (a * 50) + 6


if __name__ == "__main__":
    print(problem(12))  # 606
    print(problem("22"))  # Error
    print(problem(0))  # 6

