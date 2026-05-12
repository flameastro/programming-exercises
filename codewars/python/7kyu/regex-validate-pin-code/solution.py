# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.
# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false
# Solution
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isnumeric()


def validate_pin(pin):
    is_valid = False

    if len(pin) == 4 or len(pin) == 6:
        if pin.isnumeric():
            is_valid = True

    return is_valid


if __name__ == "__main__":
    print(validate_pin("1234"))  # True
    print(validate_pin("12345"))  # False
    print(validate_pin("a234"))  # True
