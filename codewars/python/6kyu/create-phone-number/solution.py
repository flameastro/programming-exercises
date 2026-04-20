# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
def create_phone_number(a):
    return f"({a[0]}{a[1]}{a[2]}) {a[3]}{a[4]}{a[5]}-{a[6]}{a[7]}{a[8]}{a[9]}"


if __name__ == "__main__":
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # (123) 456-7890
    print(create_phone_number([5, 4, 2, 1, 6, 5, 3, 2, 1, 5]))  # (542) 165-3215
    print(create_phone_number([5, 1, 2, 7, 4, 3, 2, 1, 0, 9]))  # 512) 743-2109
