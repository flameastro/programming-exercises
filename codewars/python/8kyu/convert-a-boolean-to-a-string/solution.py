# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.
def boolean_to_string(b):
    return str(b)

if __name__ == "__main__":
    print(boolean_to_string(True), type(boolean_to_string(True)))  # True <class 'str'>
    print(boolean_to_string(False), type(boolean_to_string(False)))  # False <class 'str'>
    print(boolean_to_string(None), type(boolean_to_string(None)))  # None <class 'str'>
